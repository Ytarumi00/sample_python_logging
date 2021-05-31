import logging
from fluent import handler

logging.basicConfig(level=logging.INFO)
l = logging.getLogger(__name__)
h = handler.FluentHandler('cat.test',  host='192.168.1.12', port=24224)
l.addHandler(h)

l.info({'from': 'userA', 'to': 'userB'})

h.close()


