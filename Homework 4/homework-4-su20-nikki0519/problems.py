import re

def problem1(searchstring):
    """
    Match phone numbers.

    :param searchstring: string
    :return: True or False
    """

    pattern1 = re.compile(r"^\(\d{3}\)\s\d{3}\-\d{4}$")
    pattern2 = re.compile(r"^\d{3}\-\d{3}\-\d{4}$")
    pattern3 = re.compile(r"^\d{3}\-\d{4}$")

    if(pattern1.fullmatch(searchstring) or pattern2.fullmatch(searchstring) or pattern3.fullmatch(searchstring)):
        return True
    else:
        return False

def problem2(searchstring):
    """
    Extract street name from address.

    :param searchstring: string
    :return: string
    """

    pattern = re.compile(r"(\d+\s)([A-Za-z\s]*)(\s\w+\.)")

    matches = pattern.finditer(searchstring)

    temp = []

    for match in matches:
        temp.append(match.group(2))

    for i in range(len(temp)):
        if(i == len(temp) - 1):
            return temp[i]

    pass
    
def problem3(searchstring):
    """
    Garble Street name.

    :param searchstring: string
    :return: string
    """

    street_name = problem2(searchstring)
    print(street_name)
    return searchstring.replace(street_name, street_name[::-1])

    pass


if __name__ == '__main__' :
    # print(problem1('7651-312')) #True
    # print(problem1('()-494-4600')) #False
    # print(problem1('7651-3152')) #False
    # print(problem1('765)-494-4600')) #True    
    # print(problem1('() 494-4600')) #True
    
    # print(problem2('The EE building is at 465 Northwestern Ave.')) #'Northwestern'
    # print(problem2('22 What A Wonderful Ave.')) #'What A Wonderful'
    # print(problem2('Go West on 999 West St.')) #West'
    # print(problem2('123 I Did not 222 Know You So Rd.')) #'Know You So'
    # print(problem2('123 West 5a Ave. 1 South St.')) #'South'
    # print(problem2('123 st. 465 Northwestern Ave.')) #'Northwestern'
    # print(problem2('123 Mayb3 Y0u 222 Did not th1nk 333 This Through Rd.')) #'This Through'
    
    # print(problem3('The EE building is at 465 Northwestern Ave.')) #'The EE building is at 465 nretsewhtroN Ave.'
    # print(problem3('22 What A Wonderful Ave.')) #'22 lufrednoW A tahW Ave.'
    # print(problem3('Go West on 999 West St.')) #'Go West on 999 tseW St.'
    # print(problem3('123 I Did not 222 Know You So Rd.')) #'123 I Did not 222 oS uoY wonK Rd.'
    # print(problem3('123 West 5a Ave. 1 South St.')) #'123 West 5a Ave. 1 htuoS St.'
    # print(problem3('123 st. 465 Northwestern Ave.')) #'123 st. 465 nretsewhtroN Ave.'
    # print(problem3('123 Mayb3 Y0u 222 Did not th1nk 333 This Through Rd.')) #'123 Mayb3 Y0u 222 Did not th1nk 333 hguorhT sihT Rd.'

    print(problem3('Go West on 999 West St.'))#=='Go West on 999 tseW St.'



