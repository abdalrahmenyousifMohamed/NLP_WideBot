# from datasets import load_dataset
import re
import numpy as np
import re

with open('local_path_to_save_vocab.txt', 'r', encoding='utf-8') as f:
    vocab = set(f.read().splitlines())


def delete_letter(word):
    return [word[:i] + word[i + 1:] for i in range(len(word))]

def switch_letter(word):
    switch_l = []

    for i in range(len(word) - 1):
        w_l = re.findall('\w', word)
        if i - 1 < 0:
            w_l[i:i + 2] = w_l[i + 1::-1]
        else:
            w_l[i:i + 2] = w_l[i + 1:i - 1:-1]

        switch_l.append(''.join(w_l))

    return switch_l

def replace_letter(word):
    letters = 'ابتةثجحخدذرزسشصضطظعغفقكلمنهويءآأؤإئ'

    replace_set = set()

    for i in range(len(word)):
        for l in letters:
            new_word = word[:i] + l + word[i + 1:]
            if new_word == word:
                continue
            replace_set.add(new_word)

    replace_l = sorted(list(replace_set))

    return replace_l

def insert_letter(word):
    letters = 'ابتةثجحخدذرزسشصضطظعغفقكلمنهويءآأؤإئ'
    insert_l = []

    for i in range(len(word) + 1):
        for l in letters:
            new_word = word[:i] + l + word[i:]
            insert_l.append(new_word)

    return insert_l

def edit_one_letter(word, allow_switches=True):
    edit_one_set = delete_letter(word) + insert_letter(word) + replace_letter(word)

    if allow_switches:
        edit_one_set += switch_letter(word)

    return set(edit_one_set)


def edit_two_letters(word, allow_switches=True):
    edit_two_set = []
    edit_one_set = edit_one_letter(word)

    for edit in edit_one_set:
        edit_two_set += edit_one_letter(edit)

    return set(edit_two_set) | set(edit_one_set)


def get_corrections(word, vocab):
    suggestions = []

    correct_word_suggest = [word] if word in vocab else []
    edit_one_letter_suggest = list(filter(lambda item: item in vocab, list(edit_one_letter(word))))
    edit_two_letter_suggest = list(filter(lambda item: item in vocab, list(edit_two_letters(word))))

    suggestions = correct_word_suggest or edit_one_letter_suggest or edit_two_letter_suggest or [
        'لم يتم العثور علي إقتراحات مناسبة لهذه الكلمة']

    return set(suggestions)


def min_edit_distance(source, target, ins_cost=1, del_cost=1, rep_cost=2):
    m = len(source)
    n = len(target)
    D = np.zeros((m + 1, n + 1), dtype=int)

    for row in range(1, m + 1):
        D[row, 0] = D[row - 1, 0] + del_cost

    for col in range(1, n + 1):
        D[0, col] = D[0, col - 1] + ins_cost

    for row in range(1, m + 1):
        for col in range(1, n + 1):
            r_cost = rep_cost

            if source[row - 1] == target[col - 1]:
                r_cost = 0

            D[row, col] = np.min([D[row - 1, col] + del_cost, D[row, col - 1] + ins_cost, D[row - 1, col - 1] + r_cost])

    med = D[m, n]

    return med


def get_suggestions(corrections, word):
    distance = []
    suggest = []

    for correction in corrections:
        source = word
        target = correction
        min_edits = min_edit_distance(source, target)

        distance.append(min_edits)
        suggest.append(correction)

    suggest_result = list(map(lambda idx: suggest[idx], np.argsort(distance)))
    return suggest_result


def ar_spelling_checker(text):
    word_l = re.findall('\w{3,}', text)
    result = {}

    for word in word_l:
        tmp_corrections = []
        if not word in vocab:
            tmp_corrections = get_corrections(word, vocab)
            if len(tmp_corrections) == 0:
                continue
            result[word] = get_suggestions(tmp_corrections, word)

    output = ''

    if len(result.keys()) == 0:
        output += 'لا توجد أخطاء إملائية '

    for word in result.keys():
        # output += f'<div class="word">{word}</div><br />'
        for suggest in result[word]:
            output += f'[{suggest}]'

        # output += '<div class="separator"></div>'

    return output


# st.markdown(
#     """
#     <style>
#         .content {
#             direction: rtl;
#         }

#         .word {
#             color: #842029;
#             background-color: #f8d7da;
#             border-color: #f5c2c7;
#             padding: 10px 20px;
#             display: inline-block;
#             direction: rtl;
#             font-size: 15px;
#             font-weight: 500;
#             margin-bottom: 15px;
#             box-sizing: border-box;
#             border: 1px solid transparent;
#             border-radius: 0.25rem;
#         }

#         .suggest {
#             color: #0f5132;
#             background-color: #d1e7dd;
#             border-color: #badbcc;
#             display: inline-block;
#             margin-right: 5px;
#         }

#         .separator {
#             height: 3px;
#             background: #CCC;
#             margin-bottom: 15px;
#         }

#         .msg {
#             color: #0f5132;
#             background-color: #d1e7dd;
#             border-color: #badbcc;
#             border: 1px solid transparent;
#             border-radius: 0.25rem;
#             padding: 15px 20px;
#             direction: rtl;
#             font-size: 20px;
#             font-weight: 500;
#             text-align: center;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# st.title("Arabic Spelling Checker ")

# st.write("Web-based app to detect spelling mistakes in Arabic words using dynamic programming")

# text = st.text_area("النص")
# btn_clicked = st.button("Spelling Check")

# if btn_clicked:
#     output = ar_spelling_checker(text)
#     st.markdown(output, unsafe_allow_html=True)
