#https://leetcode.com/problems/unique-email-addresses/

def numUniqueEmails(emails):
    out = set()
    for email in emails:
        local, domain = email.split('@')
        if '+' in local:
            local = local[:local.index('+')]
        out.add(local.replace('.','') + '@' + domain)
    return len(out)
