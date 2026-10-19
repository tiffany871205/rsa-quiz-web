import json
from pathlib import Path
items=json.loads((Path(__file__).parent/'questions.json').read_text())['items']
assert len(items)==95
assert len(set(q['uid'] for q in items))==len(items)
assert all(len(q['options'])==4 and len(set(q['options']))==4 and q['options'][q['correct']]==q['answer'] for q in items)
assert len(set(q['question'] for q in items))==len(items), '重複題目'
assert all(q.get('category') and q.get('explanation') and q.get('explanation_source') for q in items), '題目缺少分類、解析或教材來源'
assert all(q.get('source_status') and q.get('quality_review') for q in items), '題目缺少來源／審核狀態'
print('RSA: 95 valid questions')
