import sys, os
print('=== python version ===')
print(sys.version)
print('\n=== python executable ===')
print(sys.executable)
print('\n=== current working directory ===')
print(os.getcwd())
print('\n=== PYTHONPATH env var ===')
print(os.environ.get('PYTHONPATH', '<empty>'))
print('\n=== sentiment_analyzer.py present? ===')
print(os.path.exists(os.path.join(os.getcwd(), 'sentiment_analyzer.py')))
print('\n=== files in current folder (top 40) ===')
print(sorted(os.listdir(os.getcwd()))[:40])

print('\n=== try importing selected packages ===')
for pkg in ['textblob','flask','pandas','nltk','matplotlib']:
    try:
        __import__(pkg)
        print(f'{pkg}: import OK')
    except Exception as e:
        print(f'{pkg}: import FAILED — {e.__class__.__name__}: {e}')

print('\n=== installed packages (top 20) ===')
try:
    try:
        import importlib.metadata as im
        dists = list(im.distributions())[:20]
        print([(d.metadata.get('Name') or d.metadata.get('name') or 'unknown', d.version) for d in dists])
    except Exception:
        import pkg_resources
        dists = list(pkg_resources.working_set)[:20]
        print([(d.project_name, d.version) for d in dists])
except Exception as e:
    print('Could not list installed packages:', e)

print('\n=== NLTK corpora check ===')
try:
    import nltk
    try:
        nltk.data.find('tokenizers/punkt')
        print('punkt: AVAILABLE')
    except Exception:
        print('punkt: MISSING')
    try:
        nltk.data.find('corpora/stopwords')
        print('stopwords: AVAILABLE')
    except Exception:
        print('stopwords: MISSING')
except Exception as e:
    print('nltk import FAILED —', e)

print('\n=== import sentiment_analyzer module ===')
try:
    sys.path.insert(0, os.getcwd())
    import sentiment_analyzer
    print('sentiment_analyzer import: OK')
except Exception as e:
    print('sentiment_analyzer import: FAILED —', type(e).__name__, e)
