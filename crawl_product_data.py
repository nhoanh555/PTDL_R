# Import các thư viện cần thiết
import pandas as pd
import requests
import time
import random
from tqdm import tqdm

# Khai báo thông tin cookies và headers
cookies = {
    'TIKI_RECOMMENDATION': '6daf0ec0d8aeabb3461783efada3ac72',
    'TKSESSID': 'b971a21329324f186bf7f28716e4b6cf',
    'TOKENS': '{%22access_token%22:%22YcN0C1W8zP6ElLJkTgdAMyxrpvQwb94q%22}',
    '__IP': '1746718024',
    '__R': '0',
    '__iid': '749',
    '__su': '0',
    '__tb': '0',
    '__uidac': '01659576d001836f069b27e32d7a7499',
    '__uif': '__uid%3A7642940961746729271%7C__ui%3A-1%7C__create%3A1704294096',
    '__utm': 'source%3Dtiki-aff%7Cmedium%3Dtiki-aff%7Ccampaign%3DAFF_NBR_TIKIAFF_UNK_TIKIVN-D3K72LS2_ALL_VN_ALL_UNK_UNK_TAPX.f1bf430a-65cf-418a-b43e-28dfa9168045_TAPU.e8811fd7-587b-4b1d-b685-d9586955086f',
    '_fbp': 'fb.1.1704294114476.1292406438',
    '_ga': 'GA1.1.1519596821.1704294091',
    '_ga_7QN4MZMLVG': 'GS1.1.1704336969.1.1.1704336971.0.0.0',
    '_ga_L9MPNN6QJB': 'GS1.1.1704336969.1.1.1704336980.0.0.0',
    '_ga_S9GLR1RQFJ': 'GS1.1.1704334874.3.1.1704340301.60.0.0',
    '_ga_W6PZ1YEX5L': 'GS1.1.1704338649.1.1.1704339309.0.0.0',
    '_gcl_au': '1.1.737102976.1704294095',
    '_hjAbsoluteSessionInProgress': '1',
    '_hjIncludedInSessionSample_522327': '0',
    '_hjSessionUser_522327': 'eyJpZCI6IjBkZmM0NDMwLTNmYjctNTViMy1iYzc0LTc5ZjU1NjQ2Y2QxYyIsImNyZWF0ZWQiOjE3MDQyOTQwOTU5NDUsImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjSession_522327': 'eyJpZCI6ImEwNGM2ODJiLWZmZDEtNDU0Ni1iMzJlLTU3NTZiNWJhZjM4ZCIsImMiOjE3MDQzMzMwMTU4MzEsInMiOjAsInIiOjAsInNiIjowfQ',
    '_trackity': '7e2ddf92-8de0-c763-991f-c6e7161b2dac',
    'amp_99d374': '6gD267ETVSbykVTUmYnfSE...1hj92jli6.1hj99cat5.5s.8i.ee',
    'cto_bundle': 'LnIg-F83MXlqbUVEb01wcnVNeG5TTG41VkZLUG5vMjdobHlTM1JmTyUyQkt5aXczYTdXaXRta29ROWpVMHlzVWZtWnFuRGF5MlBNU0NMcSUyQmdtYlh5QVdTT3gzVk1pUklwSmZaN0hON1BjZnR2ZURLWDJtazQxWjVUS0hxY1p2S2lJZHlFNkxHQjUlMkY3ZUclMkZTWDliazFoekc5SWdQQSUzRCUzRA',
    'delivery_zone': 'Vk4wMzkwMDYwMDE=',
    'dtdz': '-1',
    'rl_anonymous_id': 'StackityEncrypt%3AU2FsdGVkX19IHHSuW%2Fa7YdscvoeaIiNu1AQ6XK0r6ed3lALdJO0T1fTAs8oSKVQWGif7Z0QECLkL3%2FZg56mQYw%3D%3D',
    'rl_group_id': 'StackityEncrypt%3AU2FsdGVkX1%2Bzr5RcL6%2BpdRK%2FM6MoTfF%2BqGSXpaziCc4%3D',
    'rl_group_trait	': 'StackityEncrypt%3AU2FsdGVkX19Raa%2FMmvCJG3SIznh%2F1j6yT4M3qjlOdPs%3D',
    'rl_page_init_referrer': 'StackityEncrypt%3AU2FsdGVkX1%2FU4RPIsBYghwLD8N1pAFHzbt6GJ3rv%2BP%2FM%2BBc3tcdL173VtWCXdYmo',
    'rl_page_init_referring_domain': 'StackityEncrypt%3AU2FsdGVkX19LlVhPZty3IE7%2FHzN5dsBc%2BTaRpnHsj%2F3JfwNfMa%2BVgsAeIbkgEjxW',
    'rl_trait': 'StackityEncrypt%3AU2FsdGVkX1%2FMH1NKb%2Bqy2ITv0sekVVS0RYOAFe9Xr2c%3D',
    'rl_user_id	': 'StackityEncrypt%3AU2FsdGVkX1%2Bivmh9WZr8a0rYPL0hPrKk%2BqDRivoA7uU%3D',
    'tiki_client_id': '1519596821.1704294091'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Referer': 'https://tiki.vn/set-2-qua-n-du-i-nam-qua-n-short-gio-nam-the-thao-basic-tre-trung-nang-do-ng-thoa-ng-ma-t-co-gia-n-4-chie-u-mrm-manlywear-p99968881.html?itm_campaign=CTP_YPD_TKA_PLA_UNK_ALL_UNK_UNK_UNK_UNK_X.284641_Y.1866961_Z.3907942_CN.03%2F2024---CB-2-Q%C4%90-Tron---Auto&itm_medium=CPC&itm_source=tiki-ads&spid=99968992',
    'x-guest-token': 'YcN0C1W8zP6ElLJkTgdAMyxrpvQwb94q',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

params = (
    ('platform', 'web'),
    ('spid', 99968992)
    #('include', 'tag,images,gallery,promotions,badges,stock_item,variants,product_links,discount_tag,ranks,breadcrumbs,top_features,cta_desktop'),
)

# Định nghĩa hàm parser để trích xuất thông tin từ phản hồi JSON
def parser_product(json):
    d = dict()
    d['id'] = json.get('id')
    d['brand_id'] = json.get('brand').get('id')
    d['brand_name'] = json.get('brand').get('name')
    d['product_name'] = json.get('name')
    d['categories'] = json.get('categories').get('name')
    d['discount'] = json.get('discount')
    d['discount_rate'] = json.get('discount_rate')
    d['list_price'] = json.get('list_price')
    d['price'] = json.get('price')
    d['rating_average'] = json.get('rating_average')
    d['review_count'] = json.get('review_count')
    d['stock_item_qty'] = json.get('stock_item').get('qty')
    d['stock_item_max_sale_qty'] = json.get('stock_item').get('max_sale_qty')
    d['short_url'] = json.get('short_url')
    return d

# Đọc danh sách ID sản phẩm từ tệp CSV
df_id = pd.read_csv('crawl_product_id.csv')
p_ids = df_id.id.to_list()
print(p_ids)

# Khởi tạo danh sách lưu trữ kết quả
result = []

# Lặp qua từng ID sản phẩm để thực hiện quá trình crawl
for pid in tqdm(p_ids, total=len(p_ids)):
    # Gửi yêu cầu API đến Tiki.vn
    response = requests.get('https://tiki.vn/api/v2/products/{}'.format(pid),
                             headers=headers, params=params, cookies=cookies)
    
    # Kiểm tra mã trạng thái phản hồi
    if response.status_code == 200:
        # In thông báo thành công và thêm kết quả vào danh sách
        print('Crawl data {} success !!!'.format(pid))
        result.append(parser_product(response.json()))
    
    # Tạm nghỉ giữa các yêu cầu để tránh gửi quá nhanh
    # time.sleep(random.randrange(3, 5))

# Tạo DataFrame từ danh sách kết quả và lưu vào tệp CSV
df_product = pd.DataFrame(result)
df_product.to_csv('crawl_product_data.csv', index=False)
