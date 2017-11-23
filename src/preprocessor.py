
import data_utils

# Training Dataset
docid, sumid, doc_dict, sum_dict = data_utils.load_data("data/train.article.txt", "data/train.title.txt", "data/doc_dict.txt", "data/sum_dict.txt", 30000, 30000)
checkid = np.random.randint(len(docid))
print(checkid)
print(docid[checkid], data_utils.sen_map2tok(docid[checkid], doc_dict[1]))
print(sumid[checkid], data_utils.sen_map2tok(sumid[checkid], sum_dict[1]))

# Validation Dataset
docid, sumid = data_utils.load_valid_data("data/valid.article.filter.txt", "data/valid.title.filter.txt", doc_dict, sum_dict)
checkid = np.random.randint(len(docid))
print(checkid)
print(docid[checkid], data_utils.sen_map2tok(docid[checkid], doc_dict[1]))
print(sumid[checkid], data_utils.sen_map2tok(sumid[checkid], sum_dict[1]))

# Testing Dataset
docid = data_utils.load_test_data("data/test.giga.txt", doc_dict)
checkid = np.random.randint(len(docid))
print(checkid)
print(docid[checkid], data_utils.sen_map2tok(docid[checkid], doc_dict[1]))
