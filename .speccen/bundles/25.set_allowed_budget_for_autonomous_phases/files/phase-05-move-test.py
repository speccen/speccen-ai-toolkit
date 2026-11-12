# Move test for phase-05-text-checks.py: for each check, move its expected text out of the place
# its Test Plan row names (in memory) and confirm that the check then fails.
import os,io,contextlib
here=os.path.dirname(os.path.abspath(__file__))
code=open(os.path.join(here,'phase-05-text-checks.py')).read()
P={'G':'skills/sdd/00-governing-workflow/SKILL.md','C':'skills/sdd/05-implementation/SKILL.md','R':'README.md'}
src={k:open(v).read() for k,v in P.items()}
def run(over):
    c=code
    for k,v in P.items(): c=c.replace(f"open('{v}').read()",f"F['{k}']")
    F=dict(src); F.update(over); buf=io.StringIO()
    try:
        with contextlib.redirect_stdout(buf): exec(c,{'F':F})
    except Exception as e: return None
    return {l.split()[0]:l.split()[1] for l in buf.getvalue().splitlines() if l.startswith('T-')}
def mv(f,a,anc,after=True):
    t=src[f]; assert t.count(a)==1,a; t=t.replace(a,'',1); assert t.count(anc)==1,anc
    return {f:t.replace(anc,anc+a if after else a+anc)}
tpl_i=src['G'].index('# speccen project configuration — committed.')
cases=[
 ('T-1',mv('G',"the current version is `3`. ","### Templates\n")),
 ('T-2',mv('G',"| `fixes` | `1` – `10` |","| `lock` | `true` · `false` |",False)),
 ('T-3',mv('G',"- `fixes`: the same five phases as `mode`. It has no effect in a `gated` phase.\n","### Effective settings\n")),
 ('T-4',{'G':src['G'][:tpl_i]+src['G'][tpl_i:].replace('    stops: inherit\n    fixes: inherit\n','    stops: inherit\n',1).replace('  close-out:                 # 06 — the audience documents run as subagents\n','  close-out:                 # 06 — the audience documents run as subagents\n    fixes: inherit\n',1)}),
 ('T-5',mv('G',", `fixes: 5` and","**Set `version`**")),
 ('T-6',mv('G',"An upgrade to version 3 adds `fixes: 5` at the top and `fixes: inherit` to the five phases that\ntake `stops`, and sets `version: 3`. An autonomous phase then makes up to five fix attempts; set\n`fixes: 1` to keep one.\n","### Effective settings\n")),
 ('T-7',mv('G',"- A `fixes` value that is not a whole number from `1` to `10` counts as `1`.\n","**Locks.**\n")),
 ('T-7',mv('G',"So is a key on a phase that does not take it","- A `prototypes` value that is not a whole number of `0` or more counts as `0`.")),
 ('T-7',{'G':src['G'].replace("is ignored and mentioned once.\n  So is a key","is an error.\n  So is a key",1)}),
 ('T-8',mv('G',"up to the phase's effective `fixes`\n  attempts (Configuration; default `5`)","  again. Rows it does not re-check keep")),
 ('T-9',mv('G',"3. a run makes no progress","  again. Rows it does not re-check keep")),
 ('T-10',mv('G',"a rule breach the run before named is still there, or more rows\n     fail than in the run before","### Stop conditions\n")),
 ('T-11',mv('G',"Log each attempt as `fix attempt <n> of <fixes>: run <N> failed rows <list>`.","### Stop conditions\n")),
 ('T-12',mv('G',"whether further fix attempts are allowed; without that, one run, and a failing row stops\n  again","  1. the fix you would make next")),
 ('T-13',mv('G',"5. a gate test still fails after the fix budget, makes no progress, or needs a fix that changes\n   a conclusion, a delegated decision or an ADR (Gate test);\n","8. this host cannot run a check the gate test requires, for example the planned tests.\n")),
 ('T-13',mv('G',"- Condition 1 is the **only** stop `proceed` removes. Conditions 2 to 8 stay hard stops: they\n  mean the basis is broken, or the action is not yours to take.\n","### Effective settings\n",False)),
 ('T-14',mv('C',"If the next\n  fix would change a phase conclusion, a delegated decision or an ADR, stop.","After two rejected iterations, stop.")),
 ('T-15',mv('C',"After two rejected iterations, stop.","### Step 1 — Stop all implementation activity immediately\n")),
 ('T-15',(lambda t:(lambda i,j:{'C':(t[:i]+t[j:]).replace('### Step 1 — Stop all implementation activity immediately\n','### Step 1 — Stop all implementation activity immediately\n'+t[i:j],1)})(t.index('- **Phase 05b.**'),t.index('- Write `## Delegate gate check`')))(src['C'])),
 ('T-16',{'R':src['R'].replace('fixes: 5\n','fixes: 2\n',1)}),
 ('T-17',mv('R',"(`inherit`, `ask`, `5`, `0`, `false`)","### Modes\n")),
 ('T-18',mv('G',"Record the self-check in one line above the gate table: `Self-check: done — N corrections`.","### Stop conditions\n")),
 ('T-19',(lambda t:(lambda i,j:{'G':(t[:i]+t[j:]).replace('### Reading and ownership\n','### Reading and ownership\n'+t[i:j],1)})(t.index('**Locks.**'),t.index('**Fail-safe')))(src['G'])),
 ('T-19',{'G':src['G'].replace('**Locks.**\n','**Locks.**\n- A lock binds `fixes` too.\n',1)}),
]
base=run({}); assert base and all(v=='PASS' for v in base.values()), base
print('unmoved text: all 19 checks pass')
bad=[]
for t,over in cases:
    r=run(over); v='FAIL (the check raised an error: its place is gone)' if r is None else r[t]
    print(t,'after move:',v)
    if v=='PASS': bad.append(t)
print('move test: every check fails after its move' if not bad else 'move test: still passing: '+', '.join(bad))
