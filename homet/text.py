with open('referat.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
    print(len(content))
    words_counter=len(content.split())
    print(words_counter)
    replacer=content.replace('.','!')
    print(replacer)
    f2=str(len(content))+str(words_counter)+str(replacer)
with open('referat2.txt', 'w', encoding='utf-8') as w:
    w.write(f2)
    print(w)

