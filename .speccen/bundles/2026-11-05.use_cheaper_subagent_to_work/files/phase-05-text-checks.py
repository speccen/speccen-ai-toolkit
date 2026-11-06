import re,subprocess
G=open('skills/sdd/00-governing-workflow/SKILL.md').read()
R=open('README.md').read(); A=open('ARCHITECTURE.md').read()
W=open('agents/speccen-worker.md').read()
C2=open('skills/sdd/02-code-analysis/SKILL.md').read(); C5=open('skills/sdd/05-implementation/SKILL.md').read()
I=open('skills/sdd/interview/SKILL.md').read()
base=lambda p: subprocess.run(['git','show','HEAD:'+p],capture_output=True,text=True).stdout
G0=base('skills/sdd/00-governing-workflow/SKILL.md')
start='```yaml\n# speccen project configuration — committed.'
def blk(s): i=s.index(start); return s[i:s.index('\n```\n',i)+5]
tg=blk(G)
def sec(s,h,nxt): i=s.index(h); return s[i:s.index(nxt,i+len(h))]
spec=sec(tg,'  specification:','  implementation:'); impl=sec(tg,'  implementation:','  close-out:')
search=sec(G,'### Search\n','### Model\n')
gate=sec(G,'### Gate test\n','### Decisions you take')
res={}
res['T-1']=('version: 2 ' in tg and 'model: economy' in spec and 'model: economy' in impl
  and 'the current version is `2`' in G and 'current version is `1`' not in G)
m=re.search(r"- `model`: (.*?) —\s+the\s+phases with subagent units",G,re.S)
res['T-2']=bool(m) and re.findall(r'`([a-z-]+)`',m.group(1))==['code-analysis','compliance-review','specification','implementation','close-out','retrospective','reference']
res['T-3']=('or a `model` on `feature-analysis`.' in G and 'a `model` on `feature-analysis`, `specification`' not in G)
res['T-4']=('| any phase (bundle and store); 02, 03, 04, 05 (code) | a **search**' in G
  and 'a search that is not launched as this unit runs inline' in G and 'Nothing else runs in a subagent. ' not in G)
order=G.index('### The worker and the work order')<G.index('### Search\n')<G.index('### Model\n')
need=['one stated question','`Outputs: none — report only`','`path:line`','verbatim quote','what was not found','no conclusions',
 're-opens every finding','never cited as evidence on its own','read-only','takes no decision','`speccen-worker`',
 'which has no `model` key','`inherit`','A search in Phase 05 uses\n`phases.implementation.model`']
miss=[n for n in need if n not in search]
res['T-5']=order and not miss
v='The gate-check verifier and every decision seat run on the session model, whatever the\nconfig says.'
res['T-6']=(v in G and v in G0 and "# Decision seats and the gate-test verifier always run on the session's model." in tg
  and '(`speccen-worker`, on the session model' in gate)
res['T-7']=all(x in gate for x in ['**Self-check before the verifier.**','1. **Quotes**','2. **References**','3. **Latest answer**','4. **Index**','5. **Interview structure**','`Self-check: done — N fixes`'])
res['T-8']=('(a) every row that failed' in gate and 'every row whose evidence is in a file you changed' in gate
  and '`confirmed (run 1)`' in gate and 'run the test again. If it still fails, stop.' not in gate)
res['T-9']='If a re-checked row still fails, stop.' in gate
res['T-10']=(C2.count('may run as search units (governing skill → Subagent Execution →\nSearch)')==2
  and C5.count('may run as a search unit (governing skill →\nSubagent Execution → Search)')==1
  and 'as a search unit (governing skill → Subagent Execution → Search)' in I and 'look it up in the code — inline, or as a search\n  unit.' in I)
res['T-11']=blk(R)==tg
sub=sec(A,'- **Subagents.**','- **Locks.**')
res['T-12']=('searches' in sub and "verifier runs in one on the session's model" in sub
  and not re.search(r'verifier\)\s+run in a `speccen-worker`\s+subagent on their tier',sub))
res['T-13']='a search, an evidence reading' in W.split('\n')[2]
def ub(s): return sec(s,'- **Add every missing key**','**Example.**')
res['T-14']=ub(G)==ub(G0) and 'a phase\'s `model` is added as `inherit`' in ub(G)
lg='Log each launched unit in `log.md`: `- **HH:MM — [PHASE] subagent** — [unit] · model:\n[tier] → [model] ([source])`.'
res['T-15']=(lg in G and lg in G0 and '`- **HH:MM — [PHASE] subagent** — search: [question] · model:\n[tier] → [model] ([source])`' in search)
res['T-16']='(`quick` · `medium` ·\n`thorough`)' in search and 'Independent searches may run in parallel' in search
mt=sec(R,'### Model tiers','\n## ')
res['T-17']="Searches (finding and quoting evidence for one question) run on the phase's tier, in Phases 02\nto 05 for code and in any phase for the bundle and store." in mt
keys=lambda s: re.findall(r'^\| `([^`]+)` \|',sec(s,'### Keys','Which phases take'),re.M)
res['T-18']=(keys(G)==keys(G0) and sec(G,'### Model\n','### Host support')==sec(G0,'### Model\n','### Host support')
  and sec(tg,'models:','```')==sec(blk(G0),'models:','```'))
res['T-19']=('nothing else, when it is upgraded to version 1:' in G
  and re.search(r'stops` on 5 phases"\.\n\nAn upgrade to version 2 also adds `model: inherit` to `specification` and `implementation`, and\nsets `version: 2`\.',G) is not None)
for k,v in res.items(): print(k,'PASS' if v else 'FAIL', ('missing: '+str(miss)) if k=='T-5' and miss else '')
