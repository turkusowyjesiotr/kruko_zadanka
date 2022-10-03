# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem?isFullScreen=true


import string


def fun(s):
    letters = list(string.ascii_letters)
    digits = list(string.digits)
    dashes = ['-', '_']
    username = []
    website = []
    extension = []
    valid = 0
    if '@' in s and '.' in s:
        try:
            username, s = s.split('@')
        except ValueError:
            return False

        try:
            website, extension = s.split('.')
        except ValueError:
            return False

        if username == '' or website == '' or extension == '':
            return False

        for char in username:
            if char not in letters + digits + dashes:
                return False
            else:
                valid = 1
        for char in website:
            if char not in letters + digits:
                return False
            else:
                valid = 1
        if len(extension) > 3:
            return False
        else:
            for char in extension:
                if char not in letters:
                    return False
                else:
                    valid = 1
        if valid == 1:
            return True
    else:
        return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)