from EksiPack.v1.app import EksiApi

eksi = EksiApi(proxy_val=True)
populer_info = eksi.get_populer_topics()
entry_info = eksi.get_entry_with_entry_id(entry_id="8780274")
topic_info = eksi.get_topic_with_topic_id(topic_id="1036065")
