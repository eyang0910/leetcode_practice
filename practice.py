# def check_same_digit(m):
#     m1_s = []
#     m2_s = []
#     # m1 = []
#     # m2 = []
#     m_s = m.split(' ')
#     # print m_s
#     for i in range(len(m_s[0])):
#         m1_s.append(m_s[0][i])
#     for j in range(len(m_s[1])):
#         m2_s.append(m_s[1][j])
#     # if sorted(m1_s) == sorted(m2_s):
#     m1_s.sort()
#     m2_s.sort()
#     # print m1_s,m2_s
#     if set(m1_s) == set(m2_s):
#         print('true')
#     else:
#         print('false')
# check_same_digit(raw_input())


def check_asym(m):
    # m_l = []
    m_a = []
    m_a2 = []
    m_l = list(m)
    # for i in range(len(m)):
    #     m_l.append(m[i])
    if len(m) % 2 != 0: #jishu
        m1 = m[0:(len(m) + 1) / 2]
        m_a.append(m1)
        m_a.append(m1[0:-1][::-1])
        m_b =int(''.join(m_a))
        # print m_b, m_a, m
        if m_b < int(m):
            c= str(int(m_a[0]) + 1)
            m_a2.append(c)
            # print m_a2
            m_a2.append((m1[0:-1][::-1]))
            # print m_a2
            m_b2 = int(''.join(m_a2))
            print m_b2
        else:
            print m_b
    else:
        m1 = m[0:(len(m)) / 2]
        m_a.append(m1)
        m_a.append(m1[::-1])
        m_b = int(''.join(m_a))
        if m_b < int(m):
            c= str(int(m_a[0]) + 1)
            m_a2.append(c)
            # print m_a2
            m_a2.append((c[::-1]))
            # print m_a2
            m_b2 = int(''.join(m_a2))
            print m_b2
        else:
            print m_b

check_asym(raw_input())
