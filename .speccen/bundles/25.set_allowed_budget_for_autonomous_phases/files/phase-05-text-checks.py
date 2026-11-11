import re,subprocess
def norm(s): return re.sub(r'\s+',' ',s)
G=open('skills/sdd/00-governing-workflow/SKILL.md').read(); g=norm(G)
C5=open('skills/sdd/05-implementation/SKILL.md').read(); c5=norm(C5)
R=open('README.md').read(); r=norm(R)
base=lambda p: subprocess.run(['git','show','a7c8206:'+p],capture_output=True,text=True).stdout
G0=base('skills/sdd/00-governing-workflow/SKILL.md'); C50=base('skills/sdd/05-implementation/SKILL.md')
start='```yaml\n# speccen project configuration — committed.'
def blk(s): i=s.index(start); return s[i:s.index('\n```\n',i)+5]
tg=blk(G)
def sec(s,h,nxt): i=s.index(h); return s[i:s.index(nxt,i+len(h))]
gate=norm(sec(G,'### Gate test\n','### Decisions you take'))
stops=norm(sec(G,'### Stop conditions\n','\n### '))
graw=sec(G,'### Gate test\n','### Decisions you take')
def bul(t,h):
    if h not in t: return ''  # the bullet is not in its place: every check on it fails
    i=t.index(h); m=re.search(r'\n(- |\n(?! ))',t[i+1:]); return norm(t[i:i+1+m.start()]) if m else norm(t[i:])
def bullet(h): return bul(graw,h)
res={}
kraw=sec(G,'### Keys\n','Which phases take which key')
vrow=[l for l in kraw.split('\n') if l.startswith('| `version` |')]
res['T-1']=len(vrow)==1 and 'the current version is `3`' in vrow[0] and 'the current version is `2`' not in g
keys=sec(G,'### Keys\n','Which phases take which key')
res['T-2']=('| `phases.<phase>.stops` | `inherit` · `ask` · `proceed` | `autonomous` only; the stop policy for one phase. `inherit` means no value at this level |\n| `fixes` | `1` – `10` |' in keys
  and 'Independent of `stops` |\n| `phases.<phase>.fixes` | `inherit` · `1` – `10` |' in keys)
which=sec(G,'Which phases take which key','The modes:')
res['T-3']='- `fixes`: the same five phases as `mode`. It has no effect in a `gated` phase.' in which
ph=re.findall(r'^  ([a-z-]+):[^\n]*\n((?:    [^\n]*\n)+)',tg,re.M)
with_fixes=[n for n,b in ph if '    stops: inherit\n    fixes: inherit\n' in b]
res['T-4']=('\nversion: 3 ' in tg and 'stops: ask\n# How many times the delegate repairs a failing gate test before it stops (autonomous only, 1–10).\n# It stops sooner when a repair makes no progress or would change a conclusion.\nfixes: 1\n' in tg
  and '#   stops       inherit · ask · proceed — autonomous only: see the top-level stops\n#   fixes       inherit · 1 – 10 — autonomous only: see the top-level fixes\n' in tg
  and with_fixes==['feature-analysis','code-analysis','compliance-review','specification','implementation']
  and tg.count('fixes: inherit')==5)
uraw=sec(G,'### Upgrading the project file\n','### Effective settings\n'); upg=norm(uraw)
absb=bul(uraw,'- **An added key keeps the effective setting unchanged**')
res['T-5']="`mode: gated`, `stops: ask`, `fixes: 1` and `lock: false` at the top; `inherit` for a phase's `mode`, `stops`, `fixes` and `model`" in absb
v2='An upgrade to version 2 also adds `model: inherit` to `specification` and `implementation`, and sets `version: 2`.'
v3='An upgrade to version 3 adds `fixes: 1` at the top and `fixes: inherit` to the five phases that take `stops`, and sets `version: 3`. Behaviour is unchanged until the Architect raises `fixes`.'
res['T-6']=v2 in upg and v3 in upg and upg.index(v3)>upg.index(v2) and upg.index(v3)-upg.index(v2)-len(v2)<=2
kl='So is a key on a phase that does not take it — a `mode` on `close-out`, `retrospective` or `reference`, or a `model` on `feature-analysis`.'
eff=sec(G,'### Effective settings\n','### Reading and ownership\n')
res_=eff.split('**Locks.**')[0]
fs=lambda t: sec(t,'**Fail-safe','### Reading and ownership\n')
kb=lambda t: bul(fs(t),'- A `phases` entry whose name is not one of the eight phase keys')
res['T-7']=('The other per-phase keys (`stops`, `fixes`, `model`, `prototypes`) resolve the same way at phase level, then fall back to their defaults (`ask`, `1`, `inherit`, `0`).' in norm(res_)
  and '- A `fixes` value that is not a whole number from `1` to `10` counts as `1`.' in fs(G) and kb(G) is not None and kb(G)==kb(G0) and kl in kb(G))
fixb=bullet('- If any item fails, fix it and run the test again')
res['T-8']="up to the phase's effective `fixes` attempts (Configuration; default `1`)" in fixb and 'fix it once and run the test again' not in g
stopb=bullet('- Stop (stop condition 5) when:')
res['T-9']=('1. the fix you would make next changes a phase conclusion, a delegated decision or an ADR' in stopb
  and '2. a re-checked row still fails and the budget is used up' in stopb and '3. a run makes no progress' in stopb)
res['T-10']=('a rule breach the run before named is still there, or more rows fail than in the run before' in gate
  and 'as many rows or more' not in g)
res['T-11']='`fix attempt <n> of <fixes>: run <N> failed rows <list>`' in gate
aft=bullet("- After a stop, the Architect's answer")
res['T-12']=('whether further fix attempts are allowed; without that, one run, and a failing row stops again' in aft
  and 'lists every rule breach it finds in that row at once' in aft
  and 'lists every rule breach it finds in that row at once' in bul(sec(G0,'### Gate test\n','### Decisions you take'),"- After a stop, the Architect's answer"))
sraw=sec(G,'### Stop conditions\n','\n### ')
c5i=norm(sraw[sraw.index('\n5. ')+1:sraw.index('\n6. ')])
hs=lambda t: bul(sec(t,'### Proceeding on a proposal\n','### Delegated decisions record\n'),'- Condition 1 is the **only** stop')
res['T-13']=(c5i=='5. a gate test still fails after the fix budget, makes no progress, or needs a fix that changes a conclusion, a delegated decision or an ADR (Gate test);'
  and 'after one fix attempt' not in g and 'Conditions 2 to 8 stay hard stops' in hs(G) and hs(G)==hs(G0))
s7=c5[c5.index('- **Step 7 (accept).**'):c5.index('- **Phase 05b.**')]
res['T-14']=("up to the phase's effective `fixes` attempts" in s7 and 'If the next fix would change a phase conclusion, a delegated decision or an ADR, stop.' in s7
  and 'If it still fails when the budget is used up, or a run makes no progress, the delegate rejects: run Phase 05b.' in s7
  and 'fix once and test again' not in c5)
op0=C50.split('\n')[26:28]; op=C5.split('\n')[26:28]
b05=lambda t: bul(sec(t,'## Mode behaviour\n','## Phase 05b — Rejection & Revert\n'),'- **Phase 05b.**')
res['T-15']='After two rejected iterations, stop.' in b05(C5) and b05(C5)==b05(C50) and op==op0
res['T-16']=blk(R)==tg
rp=R[R.index('The project file always lists every setting'):]; rp=rp[:rp.index('\n\n')]
res['T-17']='(`inherit`, `ask`, `1`, `0`, `false`)' in rp
res['T-18']='Record the self-check in one line above the gate table: `Self-check: done — N corrections`.' in bullet('- **Self-check before the verifier.**') and 'N fixes' not in G
files=subprocess.run(['git','diff','--name-only','a7c8206','--','.',':(exclude).speccen'],capture_output=True,text=True).stdout.split()
def locks(s):
    e=sec(s,'### Effective settings\n','### Reading and ownership\n')
    return sec(e,'**Locks.**','**Fail-safe') if '**Locks.**' in e else ''
res['T-19']=sorted(files)==['README.md','skills/sdd/00-governing-workflow/SKILL.md','skills/sdd/05-implementation/SKILL.md'] and locks(G)==locks(G0)
for k,v in res.items(): print(k,'PASS' if v else 'FAIL')
print('all pass' if all(res.values()) else 'FAILURES')
