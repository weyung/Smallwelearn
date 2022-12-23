import requests as r
import re


def getans(url):
    '''
    et-blank 填空题
    et-tof 判断题
    et-blank block 长填空题
    et-choice 选择题
    '''
    res = r.get(url)
    # \xc3\xa9 = é, &gt; = >, we need to escape them
    txt = res.text.encode('latin-1').decode('utf-8').replace('&gt;', '>').replace('capitolize', 'capitalize')

    pat = [r'<et-blank(?: capitalize)?>(.*?)</et-blank>',
           r'<et-tof key="(\w)">',
           r'<et-blank block>(.*?)</et-blank>',
           r'<et-choice key="(\w)">']
    pattern = [re.compile(i, re.S) for i in pat]
    answer = [re.findall(i, txt) for i in pattern]
    special = '</et-mobile-only>'
    if special in txt:
        answer = [i[:len(i)//2] for i in answer]
    return answer, txt

def anstype(ans):
    for i in len(ans):
        if not ans[i]:
            return i
    return None


if __name__ == '__main__':

    l = [[1, ['Listening', '开始学习', '用时']], [2, ['BeforeYouListen', '开始学习', '用时']], [3, ['A.Communicate', '开始学习', '用时07:07']], [3, ['B.ThinkCritically', '开始学习', '用时00:00']], [3, ['C.Vocabulary', '开始学习', '用时14:08']], [2, ['Listen', '开始学习', '用时']], [3, ['D.ListenforMainIdeas', '开始学习', '用时00:24']], [3, ['E.ListenforDetails', '开始学习', '用时00:00']], [3, ['ListeningSkill', '开始学习', '用时00:00']], [3, ['ExerciseF', '开始学习', '用时00:00']], [3, ['Note-TakingSkill', '开始学习', '用时00:00']], [3, ['G.ListenandTakeNotes', '开始学习', '用时00:02']], [1, ['ExtendedListening', '开始学习', '用时']], [2, ['Passage1', '开始学习', '用时']], [3, ['NewWordsandExpressions', '开始学习', '用时00:00']], [3, ['ExerciseA', '开始学习', '用时00:00']], [3, ['ListeningSkill', '开始学习', '用时00:00']], [3, ['ExerciseB', '开始学习', '用时01:00']], [2, ['Passage2', '开始学习', '用时']], [3, ['NewWordsandExpressions', '开始学习', '用时00:00']], [3, ['ExerciseC', '开始学习', '用时00:00']], [3, ['ExerciseD', '开始学习', '用时00:00']], [2,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ['Lecture(I)', ' 开始学习', '用时']], [3, ['NewWordsandExpressions', '开始学习', '用时00:00']], [3, ['ExerciseE', '开始学习', '用时00:00']], [3, ['ExerciseF', '开始学习', '用时00:00']], [2, ['Lecture(II)', '开始学习', '用时']], [3, ['NewWordsandExpressions', '开始学习', '用时00:00']], [3, ['ExerciseG', '开始学习', '用时00:00']], [3, ['ExerciseH', '开始学习', '用时00:00']], [1, ['Speaking', '开始学习', '用时']], [2, ['SpeakingSkill', '开始学习', '用时00:00']], [2, ['B.Communicate', '开始学习', '用时00:00']], [2, ['PronunciationSkill', '开始学习', '用时00:00']], [2, ['ExerciseC', '开始学习', '用时00:00']], [1, ['TEDTalks', '开始学习', '用时']], [2, ['BeforeYouWatch', '开始学习', '用时']], [3, ['A.Communicate', '开始学习', '用时00:00']], [3, ['C.Vocabulary', '开始学习', '用时00:00']], [2, ['Watch', '开始学习', '用时']], [3, ['D.WatchforMainIdeas', '开始学习', '用时00:00']], [3, ['E.WatchforDetails', '开始学习', '用时00:00']], [3, ['F.IdentifyExamples', '开始学习', '用时00:00']], [3, ['G.ExpandYourVocabulary', '开始学习', '用时00:00']], [1, ['Presentation', '开始学习', '用时']], [2, ['Presentation', '开始学习', '用时00:00']], [1, ['Self-test', '开始学习', '用时']], [2, ['Self-test', '开始学习', '用时00:00']]]
    for i in l:
        print(i)

    idx = [0, 0, 0]
    cs = {}
    for i in l:
        if i[0] == 1:
            idx[0] += 1
            idx[1] = 0
            idx[2] = 0
            cs['{}'.format(idx[0])] = i[1]
        elif i[0] == 2:
            idx[1] += 1
            idx[2] = 0
            cs['{}-{}'.format(idx[0], idx[1])] = i[1]
        elif i[0] == 3:
            idx[2] += 1
            cs['{}-{}-{}'.format(idx[0], idx[1], idx[2])] = i[1]
        else:
            raise Exception('error')
    for i in cs:
        print(i)
        url = 'https://centercourseware.sflep.com/New College English Viewing Listening Speaking 3/data/1/%s.html' % i
        res = getans(url)
        print(res)
