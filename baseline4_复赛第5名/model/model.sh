!CUDA_VISIBLE_DEVICES=0 python src/run_bert_base_fgm.py \
--model_type bert \
--model_name_or_path src/chinese_roberta_wwm_large_ext_pytorch  \
--do_train \
--do_eval \
--do_test \
--data_dir dataset/data_gitignore/data_StratifiedKFold_42/data_origin_swap_q1q2_0 \
--output_dir ./1120_roberta_wwm_large_150_last2embedding_cls/1120_roberta_wwm_large_150_last2embedding_cls_0 \
--max_seq_length 150 \
--split_num 1 \
--lstm_hidden_size 512 \
--lstm_layers 1 \
--lstm_dropout 0.1 \
--eval_steps 200 \
--per_gpu_train_batch_size 4 \
--gradient_accumulation_steps 1 \
--warmup_steps 0 \
--per_gpu_eval_batch_size 128 \
--learning_rate 1e-5 \
--adam_epsilon 1e-6 \
--weight_decay 0 \
--train_steps 30000 \
--freeze 0 \
--is_first_eval 0 \
--not_do_eval_steps 0.7

!CUDA_VISIBLE_DEVICES=0 python src/run_bert_base_fgm.py \
--model_type bert \
--model_name_or_path src/chinese_roberta_wwm_large_ext_pytorch  \
--do_train \
--do_eval \
--do_test \
--data_dir dataset/data_gitignore/data_StratifiedKFold_42/data_origin_swap_q1q2_1 \
--output_dir ./1120_roberta_wwm_large_150_last2embedding_cls/1120_roberta_wwm_large_150_last2embedding_cls_1 \
--max_seq_length 150 \
--split_num 1 \
--lstm_hidden_size 512 \
--lstm_layers 1 \
--lstm_dropout 0.1 \
--eval_steps 200 \
--per_gpu_train_batch_size 4 \
--gradient_accumulation_steps 1 \
--warmup_steps 0 \
--per_gpu_eval_batch_size 128 \
--learning_rate 1e-5 \
--adam_epsilon 1e-6 \
--weight_decay 0 \
--train_steps 30000 \
--freeze 0 \
--is_first_eval 0 \
--not_do_eval_steps 0.7

!CUDA_VISIBLE_DEVICES=0 python src/run_bert_base_fgm.py \
--model_type bert \
--model_name_or_path src/chinese_roberta_wwm_large_ext_pytorch  \
--do_train \
--do_eval \
--do_test \
--data_dir dataset/data_gitignore/data_StratifiedKFold_42/data_origin_swap_q1q2_2 \
--output_dir ./1120_roberta_wwm_large_150_last2embedding_cls/1120_roberta_wwm_large_150_last2embedding_cls_2 \
--max_seq_length 150 \
--split_num 1 \
--lstm_hidden_size 512 \
--lstm_layers 1 \
--lstm_dropout 0.1 \
--eval_steps 200 \
--per_gpu_train_batch_size 4 \
--gradient_accumulation_steps 1 \
--warmup_steps 0 \
--per_gpu_eval_batch_size 128 \
--learning_rate 1e-5 \
--adam_epsilon 1e-6 \
--weight_decay 0 \
--train_steps 30000 \
--freeze 0 \
--is_first_eval 0 \
--not_do_eval_steps 0.7

!CUDA_VISIBLE_DEVICES=0 python src/run_bert_base_fgm.py \
--model_type bert \
--model_name_or_path src/chinese_roberta_wwm_large_ext_pytorch  \
--do_train \
--do_eval \
--do_test \
--data_dir dataset/data_gitignore/data_StratifiedKFold_42/data_origin_swap_q1q2_3 \
--output_dir ./1120_roberta_wwm_large_150_last2embedding_cls/1120_roberta_wwm_large_150_last2embedding_cls_3 \
--max_seq_length 150 \
--split_num 1 \
--lstm_hidden_size 512 \
--lstm_layers 1 \
--lstm_dropout 0.1 \
--eval_steps 200 \
--per_gpu_train_batch_size 4 \
--gradient_accumulation_steps 1 \
--warmup_steps 0 \
--per_gpu_eval_batch_size 128 \
--learning_rate 1e-5 \
--adam_epsilon 1e-6 \
--weight_decay 0 \
--train_steps 30000 \
--freeze 0 \
--is_first_eval 0 \
--not_do_eval_steps 0.7

!CUDA_VISIBLE_DEVICES=0 python src/run_bert_base_fgm.py \
--model_type bert \
--model_name_or_path src/chinese_roberta_wwm_large_ext_pytorch  \
--do_train \
--do_eval \
--do_test \
--data_dir dataset/data_gitignore/data_StratifiedKFold_42/data_origin_swap_q1q2_4 \
--output_dir ./1120_roberta_wwm_large_150_last2embedding_cls/1120_roberta_wwm_large_150_last2embedding_cls_4 \
--max_seq_length 150 \
--split_num 1 \
--lstm_hidden_size 512 \
--lstm_layers 1 \
--lstm_dropout 0.1 \
--eval_steps 200 \
--per_gpu_train_batch_size 4 \
--gradient_accumulation_steps 1 \
--warmup_steps 0 \
--per_gpu_eval_batch_size 128 \
--learning_rate 1e-5 \
--adam_epsilon 1e-6 \
--weight_decay 0 \
--train_steps 30000 \
--freeze 0 \
--is_first_eval 0 \
--not_do_eval_steps 0.7

