for i in {0..7}
do
  uv run scripts/score_cluster.py --cluster_name cluster${i} --enable_logprobs
done
