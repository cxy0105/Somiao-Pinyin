import regex
import string

PUNCTUATION = "＂＃＄％＆＇（）＊＋－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏."+string.punctuation


def sentence_clean(text):
    text = regex.sub("[A-Za-z0-9]", "", text)
    text = regex.sub("\s", "", text)
    text = regex.sub(u"[^ \p{Han}。，！？]", "", text)
    text = regex.sub('['+PUNCTUATION+']', "", text)
    text = regex.sub("。.*", "。", text)
    text = regex.sub("，.*", "，", text)
    text = regex.sub("？.*", "？", text)
    text = regex.sub("！.*", "！", text)
    text = regex.sub("嚒", "么", text)
    text = regex.sub("艹", "草", text)
    text = regex.sub("𥚃", "里", text)
    return text


def main():
    fout = open('./data/format.txt', 'w', encoding='utf-8')
    with open('./data/sentences.txt', 'r', encoding='utf-8') as fin:
        i = 1
        for line in fin:
            line = sentence_clean(line.strip())
            if line == '' or len(line) > 25:
                continue
            line = str(i) + "\t" + line + "\n"
            fout.write(line)
            i = i + 1
    fout.close()


if __name__ == '__main__':
    main()
    print("Done")
