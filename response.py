def best_practices(data):
    print(data['lighthouseResult']['audits']['is-on-https']['title'])

def seo_audit(data):
    print(data['lighthouseResult']['audits']['robots-txt']['title'])