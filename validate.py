import json
import hashlib
from collections import Counter
from pathlib import Path
items=json.loads((Path(__file__).parent/'questions.json').read_text())['items']
assert len(items)==95
assert len(set(q['uid'] for q in items))==len(items)
assert all(len(q['options'])==4 and len(set(q['options']))==4 and q['options'][q['correct']]==q['answer'] for q in items)
assert len(set(q['question'] for q in items))==len(items), '重複題目'
assert all(q.get('category') and q.get('explanation') and q.get('explanation_source') for q in items), '題目缺少分類、解析或教材來源'
assert all(q.get('source_status') and q.get('quality_review') for q in items), '題目缺少來源／審核狀態'
assert all(q['uid']=='rsa-'+hashlib.sha256(q['question'].encode()).hexdigest()[:16] for q in items), 'UID 不符合題目內容'
assert all(q['id']==i for i,q in enumerate(items,1)), '題目 ID 非連續'
assert all(isinstance(q['correct'],int) and 0<=q['correct']<4 for q in items), '答案索引不合法'
assert all(q['section']=='資安觀念' and '補充通用資安知識' in q['source_status'] for q in items if q['category'].startswith('資安知識')), '通用資安題標記錯誤'
assert all(q['section']!='資安觀念' for q in items if not q['category'].startswith('資安知識')), '教材題被誤標為通用知識'
print(f'RSA: {len(items)} valid questions; categories: {len(Counter(q["category"] for q in items))}')
