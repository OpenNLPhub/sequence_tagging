import os
from pathlib import Path
BASE_DIR = Path('slot_extraction')
bert_config = {
    'data_dir':'data',
    'vocab_file':"vocab.txt",
    'embedding_dir':os.path.join('data','embedding_data'),
    'embedding_file_name':"sgns.financial.bigram-char",
    # 'input_embedding_file':"bert_input_char_embedding.npy",
    'input_word_embedding_file':"bert_input_word_embedding.npy",
    'slot_list_root_path':os.path.join('data','slot_pattern'),
    'slot_file_name':"tmp_slot_list",
    'bert_slot_file_name':"bert_slot_pattern",
    'bert_slot_complete_file_name':"bert_complete_slot_pattern",
    'log_dir': os.path.join('output','log'),
    'data_file_name':'orig_data_train.txt',
    'seg_train_data_json':'data/seg_orig_data_train.json',
    'seg_dev_data_json':'data/seg_orig_data_dev.json',
    'seg_test_data_json':'data/seg_orig_data_test.json',
    'train_valid_data_dir':'word_train_valid_data_bert',
    'train_data_text_name':'train_split_data_text.npy',
    'valid_data_text_name':'valid_split_data_text.npy',
    'train_data_tag_name':'train_split_data_tag.npy',
    'valid_data_tag_name':'valid_split_data_tag.npy',
    'test_data_text_name':'test_data_text.npy',
    'test_data_tag_name':'test_data_tag.npy',
    'train_data_text_word_name':'train_bert_word_split_data.npy',
    'valid_data_text_word_name':'valid_bert_word_split_data.npy',
    'test_data_text_word_name':'test_bert_word_split_data.npy',
    'orig_dev':'orig_data_dev.txt',
    'orig_test':'orig_data_test.txt',
    "standard_slot_description":os.path.join('data','slot_pattern','slot_description.csv'),
    "bert_pretrained_model_path":os.path.join('data','chinese_roberta_wwm_ext_L-12_H-768_A-12'),
    # "bert_pretrained_model_path":os.path.join('data','chinese_roberta_wwm_ext_pytorch'),
    "bert_config_path":"bert_config.json",
    'bert_init_checkpoints':'bert_model.ckpt',
    "bert_model_dir":os.path.join('output','model','bert_model','checkpoint'),
    "bert_model_pb":os.path.join('output','model','bert_model','saved_model'),
    "bert_mwa_model_dir":os.path.join('output','model','bert_mwa_model','checkpoint'),
    "bert_mwa_model_pb":os.path.join('output','model','bert_mwa_model','saved_model'),
    "bert_mwa_torch_model_dir":os.path.join('output','model','bert_mwa_torch_model'),
    "bert_mwa_nocrf_torch_model_dir":os.path.join('output','model','bert_mwa_nocrf_torch_model'),
    "bert_crf_torch_model_dir":os.path.join('output','model','bert_crf_torch_model'),
    "bert_nocrf_torch_model_dir":os.path.join('output','model','bert_nocrf_torch_model'),
    "bert_mwa_nocrf_dropout_torch_model_dir":os.path.join('output','model','bert_mwa_nocrf_dropout_torch_model'),
    "bert_mwa_nocrf_warmup_dropout_torch_model_dir":os.path.join('output','model','bert_mwa_nocrf_warmup_dropout_torch_model'),
    "bert_mwa_nocrf_warmup_1head_dropout_torch_model_dir":os.path.join('output','model','bert_mwa_nocrf_warmup_1head_dropout_torch_model'),
    "bert_mwa_crf_warmup_1head_dropout_torch_model_dir":os.path.join('output','model','bert_mwa_crf_warmup_1head_dropout_torch_model'),
    "bert_mwa_crf_warmup_1head_1baidulac_dropout_torch_model_dir":os.path.join('output','model','bert_mwa_crf_warmup_1head_1baidulac_dropout_torch_model')

}
# print(os.path.join(config.get("train_valid_data_dir"),config.get("train_data_text_name")))