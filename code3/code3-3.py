import re

with open("callcenter20250301.log", "r", encoding="utf-8") as f:
    content = f.read()
pattern = re.compile(r"(\d{6})-(\d{7})")
masked_content = pattern.sub(r"\1-*******", content)

with open("callcenter20250301_masked.log", "w", encoding="utf-8") as f:
    f.write(masked_content)
print(
    '주민등록번호 마스킹 완료. "callcenter20250301_masked.log.txt" 파일로 저장되었습니다.'
)
