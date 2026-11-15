import re,subprocess,glob
BASE='67c6ad8'  # the last commit before the skill edits
def norm(s): return re.sub(r'\s+',' ',s)
def rd(p): return open(p).read()
G=rd('skills/sdd/00-governing-workflow/SKILL.md'); g=norm(G)
I=rd('skills/sdd/interview/SKILL.md'); i=norm(I)
P=rd('skills/sdd/05-implementation/SKILL.md'); p=norm(P)
R=rd('skills/sdd/reconcile/SKILL.md'); r=norm(R)
M=rd('README.md'); m=norm(M)
def sec(s,h,nxt): a=s.index(h); return s[a:s.index(nxt,a+len(h))]
sq=sec(G,'### Structured questions\n','\n---\n'); sqn=norm(sq)
gate=norm(sec(G,'### Gate test\n','### Decisions you take'))
stops=norm(sec(G,'### Stop conditions\n','\n### '))
res={}

# R-1: one rule, at the end of Structured questions, after "A series of decisions"
rule_i=sqn.find('**Subjects: `[INTERNAL-NUMBER | HUMAN UNDERSTANDABLE TEXT]`.**')
res['T-1']=(rule_i>sqn.index('**A series of decisions**')
  and sqn.rstrip().endswith('the fix-attempt log line.')
  and 'A label never stands alone.' in sqn
  and '`[01/7 | Which queue carries the retry?]`' in sqn
  and "`[DD-4 | Does the fix budget also cover Phase 05's own fix rule?]`" in sqn
  and all(k in sqn[rule_i:] for k in ['`DD-<n>`','`01/<n>`','`<skill>/<n>`','`Deviation [N]`','`O-<n>`','`H-<n>`','`P02-<n>`','a gate-check row','any number a bundle gives its items']))
# R-1, R-2, R-3: the bullets
tail=sqn[rule_i:]
res['T-2']=('In an `AskUserQuestion` call, question text that names an item gives it a subject; the header is exempt.' in tail
  and 'Inside a markdown table, write the subject\'s bar as `\\|`.' in tail
  and 'Records are not questions and keep their form: the gate-check, delegated-decision and interview tables, the Retrospective\'s delegation findings, and the fix-attempt log line.' in tail)
# R-1: defined once
cnt=sum(rd(f).count('HUMAN UNDERSTANDABLE TEXT') for f in glob.glob('skills/**/*.md',recursive=True))
res['T-3']=cnt==1
# R-4: round template
res['T-4']=('**[01/7 | The decision, as a plain question]**' in I and '**[01/8 | …]**' in I and '[Short title]' not in I
  and re.search(r'- \*\*One decision per question\*\*[^\n]*\n   - \*\*Subject format\*\* \(governing skill → Structured questions\)',I) is not None)
# R-5: review round
res['T-5']=('One question per delegated decision**, with the subject `[DD-<n> | what was decided]`, then why' in i
  and '(`DD-<n>`): `adopt`' not in i and 'Put the `MATERIAL — unconfirmed` decisions first.' in i)
# R-6..R-13
res['T-6']='an open item with the exact question, the options, your lean and the evidence — every item with a `[number | text]` subject, readable without the rest of the bundle (Structured questions);' in stops
res['T-7']='Then report to the Architect in one message, with `[number | text]` subjects (Structured questions): the phases run,' in g
res['T-8']=('for the six common failures' in gate and '6. **Subjects** — every question and item put to the Architect has a `[number | text]` subject; no label stands alone.' in gate
  and 'five common failures' not in g)
res['T-9']='under its open items, with a `[number | text]` subject (Structured questions).' in g
res['T-10']='any pending graduation proposal — each named with a `[number | text]` subject (Structured questions)' in g
res['T-11']="in the Architect's words where possible, each with its `[number | text]` subject (governing skill → Structured questions)." in i
res['T-12']='[or: with the following waived: > [T-<n> | what the test checks], …]' in p
res['T-13']='`Stopped (autonomous) — <one-line reason>`, where an item the reason names has its `[number | text]` subject;' in stops
res['T-14']=('[id-A | what it decides] and [id-B | what it decides] both govern' in r
  and 'items needing human resolution, each with a `[id | text]` subject (governing skill → Structured questions), pointing them at' in r)
# R-15
arch=subprocess.run(['git','diff','--quiet',BASE,'--','ARCHITECTURE.md']).returncode==0
auto=norm(sec(M,'**It stops when your recorded intent does not decide**','### The project defaults'))
res['T-15']=('each item named as `[number | text]` so you can answer from the message alone' in auto
  and 'each delegated decision, named as `[DD-<n> | what was decided]`' in auto and arch)
# R-16
res['T-16']=('1. the fix you would make next changes a phase conclusion, an ADR, or what a delegated decision decides; or' in gate
  and gate.find('A fix that only repairs how a decision is recorded is not such a change: splitting a question into one per decision with the same answer each, moving a question to the round its dependencies allow, correcting a citation, or raising a decision\'s materiality to `MATERIAL — unconfirmed`. Each new or changed entry keeps the decision\'s answer and states the repair; the review round still puts every one of them to the Architect.')
     not in (-1,) and gate.find('A fix that only repairs') < gate.find('Log each attempt as'))
res['T-17']=('needs a fix that changes a conclusion, an ADR or what a delegated decision decides (Gate test);' in stops
  and 'If the next fix would change a phase conclusion, an ADR, or what a delegated decision decides, stop' in p
  and 'a delegated decision or an ADR' not in g and 'a delegated decision or an ADR' not in p)
start='```yaml\n# speccen project configuration — committed.'
def blk(s): a=s.index(start); return s[a:s.index('\n```\n',a)+5]
cmt='# It stops sooner when a repair makes no progress, or would change a conclusion, an ADR\n# or what a delegated decision decides.\n'
res['T-18']=cmt in blk(G) and blk(G)==blk(M)
# R-2, R-17: unchanged passages
base=lambda f: subprocess.run(['git','show',BASE+':'+f],capture_output=True,text=True).stdout
G0=base('skills/sdd/00-governing-workflow/SKILL.md'); I0=base('skills/sdd/interview/SKILL.md')
tool=lambda s: sec(s,'The tool\'s real constraints (Claude Code):','**Two failure modes')
numb=lambda s: sec(s,'## Numbering','\n## ')
res['T-19']=(tool(G)==tool(G0) and numb(I)==numb(I0)
  and 'Log each attempt as `fix attempt <n> of <fixes>: run <N> failed rows <list>`.' in gate
  and 'Conditions 2 to 8 stay hard stops' in g)
# R-4, R-17
stat=subprocess.run(['git','diff','--name-only',BASE,'--','.',':!.speccen'],capture_output=True,text=True).stdout.split()
res['T-20']=sorted(stat)==sorted(['README.md','skills/sdd/00-governing-workflow/SKILL.md','skills/sdd/05-implementation/SKILL.md','skills/sdd/interview/SKILL.md','skills/sdd/reconcile/SKILL.md'])

for k in sorted(res,key=lambda x:int(x[2:])): print(k,'PASS' if res[k] else 'FAIL')
print('ALL PASS' if all(res.values()) else 'FAILURES')
