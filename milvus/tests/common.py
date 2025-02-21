# (C) Datadog, Inc. 2024-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

from datadog_checks.dev import get_docker_hostname, get_here

HERE = get_here()
HOST = get_docker_hostname()
PORT = 9091


def get_fixture_path(filename):
    return os.path.join(HERE, 'fixtures', filename)


MOCKED_INSTANCE = {
    "openmetrics_endpoint": f"http://{HOST}:{PORT}/metrics",
    'tags': ['test:tag'],
}

COMPOSE_FILE = os.path.join(HERE, 'compose', 'docker-compose.yaml')

STANDALONE_TEST_METRICS = {
    'milvus.go.gc_duration_seconds.quantile': 'gauge',
    'milvus.go.gc_duration_seconds.sum': 'monotonic_count',
    'milvus.go.gc_duration_seconds.count': 'monotonic_count',
    'milvus.go.goroutines': 'gauge',
    'milvus.go.info': 'gauge',
    'milvus.go.memstats.alloc_bytes': 'gauge',
    'milvus.go.memstats.alloc_bytes.count': 'monotonic_count',
    'milvus.go.memstats.buck_hash_sys_bytes': 'gauge',
    'milvus.go.memstats.frees.count': 'monotonic_count',
    'milvus.go.memstats.gc_sys_bytes': 'gauge',
    'milvus.go.memstats.heap.alloc_bytes': 'gauge',
    'milvus.go.memstats.heap.idle_bytes': 'gauge',
    'milvus.go.memstats.heap.inuse_bytes': 'gauge',
    'milvus.go.memstats.heap.objects': 'gauge',
    'milvus.go.memstats.heap.released_bytes': 'gauge',
    'milvus.go.memstats.heap.sys_bytes': 'gauge',
    'milvus.go.memstats.last_gc_time_seconds': 'gauge',
    'milvus.go.memstats.lookups.count': 'monotonic_count',
    'milvus.go.memstats.mallocs.count': 'monotonic_count',
    'milvus.go.memstats.mcache.inuse_bytes': 'gauge',
    'milvus.go.memstats.mcache.sys_bytes': 'gauge',
    'milvus.go.memstats.mspan.inuse_bytes': 'gauge',
    'milvus.go.memstats.mspan.sys_bytes': 'gauge',
    'milvus.go.memstats.next_gc_bytes': 'gauge',
    'milvus.go.memstats.other_sys_bytes': 'gauge',
    'milvus.go.memstats.stack.inuse_bytes': 'gauge',
    'milvus.go.memstats.stack.sys_bytes': 'gauge',
    'milvus.go.memstats.sys_bytes': 'gauge',
    'milvus.go.threads': 'gauge',
    'milvus.cgo.active_future_total': 'gauge',
    'milvus.cgo.cgo_duration_seconds.sum': 'monotonic_count',
    'milvus.cgo.cgo_duration_seconds.count': 'monotonic_count',
    'milvus.cgo.cgo_duration_seconds.bucket': 'monotonic_count',
    'milvus.cgo.cgo_queue_duration_seconds.sum': 'monotonic_count',
    'milvus.cgo.cgo_queue_duration_seconds.count': 'monotonic_count',
    'milvus.cgo.cgo_queue_duration_seconds.bucket': 'monotonic_count',
    'milvus.cgo.running_cgo_call_total': 'gauge',
    'milvus.datacoord.collection_num': 'gauge',
    'milvus.datacoord.consume_datanode_tt_lag_ms': 'gauge',
    'milvus.datacoord.datanode_num': 'gauge',
    'milvus.datacoord.import_tasks': 'gauge',
    'milvus.datacoord.index.task': 'gauge',
    'milvus.datacoord.index.node_num': 'gauge',
    'milvus.datacoord.index.req.count': 'monotonic_count',
    'milvus.datacoord.segment_num': 'gauge',
    'milvus.datacoord.task_execute_max_latency.sum': 'monotonic_count',
    'milvus.datacoord.task_execute_max_latency.count': 'monotonic_count',
    'milvus.datacoord.task_execute_max_latency.bucket': 'monotonic_count',
    'milvus.datanode.autoflush_buffer_op.count': 'monotonic_count',
    'milvus.datanode.consume.bytes.count': 'monotonic_count',
    'milvus.datanode.encode_buffer_latency.sum': 'monotonic_count',
    'milvus.datanode.encode_buffer_latency.count': 'monotonic_count',
    'milvus.datanode.encode_buffer_latency.bucket': 'monotonic_count',
    'milvus.datanode.flowgraph_num': 'gauge',
    'milvus.datanode.flush.buffer_op.count': 'monotonic_count',
    'milvus.datanode.flush.req.count': 'monotonic_count',
    'milvus.datanode.flushed_data.rows.count': 'monotonic_count',
    'milvus.datanode.flushed_data.size.count': 'monotonic_count',
    'milvus.datanode.msg.rows.count': 'monotonic_count',
    'milvus.datanode.save_latency.sum': 'monotonic_count',
    'milvus.datanode.save_latency.count': 'monotonic_count',
    'milvus.datanode.save_latency.bucket': 'monotonic_count',
    'milvus.flushed_segment_file_num.sum': 'monotonic_count',
    'milvus.flushed_segment_file_num.count': 'monotonic_count',
    'milvus.flushed_segment_file_num.bucket': 'monotonic_count',
    'milvus.indexnode.build_index_latency.sum': 'monotonic_count',
    'milvus.indexnode.build_index_latency.count': 'monotonic_count',
    'milvus.indexnode.build_index_latency.bucket': 'monotonic_count',
    'milvus.indexnode.encode_index_latency.sum': 'monotonic_count',
    'milvus.indexnode.encode_index_latency.count': 'monotonic_count',
    'milvus.indexnode.encode_index_latency.bucket': 'monotonic_count',
    'milvus.indexnode.index.task.count': 'monotonic_count',
    'milvus.indexnode.index.task_latency_in_queue.count': 'monotonic_count',
    'milvus.indexnode.index.task_latency_in_queue.sum': 'monotonic_count',
    'milvus.indexnode.index.task_latency_in_queue.bucket': 'monotonic_count',
    'milvus.indexnode.knowhere_build_index_latency.sum': 'monotonic_count',
    'milvus.indexnode.knowhere_build_index_latency.count': 'monotonic_count',
    'milvus.indexnode.knowhere_build_index_latency.bucket': 'monotonic_count',
    'milvus.indexnode.save_index_latency.sum': 'monotonic_count',
    'milvus.indexnode.save_index_latency.count': 'monotonic_count',
    'milvus.indexnode.save_index_latency.bucket': 'monotonic_count',
    'milvus.meta.kv_size.sum': 'monotonic_count',
    'milvus.meta.kv_size.count': 'monotonic_count',
    'milvus.meta.kv_size.bucket': 'monotonic_count',
    'milvus.meta.op.count': 'monotonic_count',
    'milvus.meta.request_latency.sum': 'monotonic_count',
    'milvus.meta.request_latency.count': 'monotonic_count',
    'milvus.meta.request_latency.bucket': 'monotonic_count',
    'milvus.msg_queue_consumer_num': 'gauge',
    'milvus.msgstream.op.count': 'monotonic_count',
    'milvus.msgstream.request_latency.sum': 'monotonic_count',
    'milvus.msgstream.request_latency.count': 'monotonic_count',
    'milvus.msgstream.request_latency.bucket': 'monotonic_count',
    'milvus.num_node': 'gauge',
    'milvus.proxy.apply.pk_latency.sum': 'monotonic_count',
    'milvus.proxy.apply.pk_latency.count': 'monotonic_count',
    'milvus.proxy.apply.pk_latency.bucket': 'monotonic_count',
    'milvus.proxy.apply.timestamp_latency.sum': 'monotonic_count',
    'milvus.proxy.apply.timestamp_latency.count': 'monotonic_count',
    'milvus.proxy.apply.timestamp_latency.bucket': 'monotonic_count',
    'milvus.proxy.assign_segmentID_latency.sum': 'monotonic_count',
    'milvus.proxy.assign_segmentID_latency.count': 'monotonic_count',
    'milvus.proxy.assign_segmentID_latency.bucket': 'monotonic_count',
    'milvus.proxy.cache.hit.count': 'monotonic_count',
    'milvus.proxy.cache.update_latency.sum': 'monotonic_count',
    'milvus.proxy.cache.update_latency.count': 'monotonic_count',
    'milvus.proxy.cache.update_latency.bucket': 'monotonic_count',
    'milvus.proxy.delete_vectors.count': 'monotonic_count',
    'milvus.proxy.msgstream_obj_num': 'gauge',
    'milvus.proxy.mutation_send_latency.sum': 'monotonic_count',
    'milvus.proxy.mutation_send_latency.count': 'monotonic_count',
    'milvus.proxy.mutation_send_latency.bucket': 'monotonic_count',
    'milvus.proxy.rate_limit_req.count': 'monotonic_count',
    'milvus.proxy.report_value.count': 'monotonic_count',
    'milvus.proxy.req.count': 'monotonic_count',
    'milvus.proxy.req.in_queue_latency.sum': 'monotonic_count',
    'milvus.proxy.req.in_queue_latency.count': 'monotonic_count',
    'milvus.proxy.req.in_queue_latency.bucket': 'monotonic_count',
    'milvus.proxy.req.latency.sum': 'monotonic_count',
    'milvus.proxy.req.latency.count': 'monotonic_count',
    'milvus.proxy.req.latency.bucket': 'monotonic_count',
    'milvus.proxy.send_bytes.count': 'monotonic_count',
    'milvus.proxy.sq.decode_result_latency.sum': 'monotonic_count',
    'milvus.proxy.sq.decode_result_latency.count': 'monotonic_count',
    'milvus.proxy.sq.decode_result_latency.bucket': 'monotonic_count',
    'milvus.proxy.sq.reduce_result_latency.sum': 'monotonic_count',
    'milvus.proxy.sq.reduce_result_latency.count': 'monotonic_count',
    'milvus.proxy.sq.reduce_result_latency.bucket': 'monotonic_count',
    'milvus.proxy.sq.wait_result_latency.sum': 'monotonic_count',
    'milvus.proxy.sq.wait_result_latency.count': 'monotonic_count',
    'milvus.proxy.sq.wait_result_latency.bucket': 'monotonic_count',
    'milvus.proxy.sync_segment_request_length.sum': 'monotonic_count',
    'milvus.proxy.sync_segment_request_length.count': 'monotonic_count',
    'milvus.proxy.sync_segment_request_length.bucket': 'monotonic_count',
    'milvus.proxy.tt_lag_ms': 'gauge',
    'milvus.querycoord.collection_num': 'gauge',
    'milvus.querycoord.load.latency.sum': 'monotonic_count',
    'milvus.querycoord.load.latency.count': 'monotonic_count',
    'milvus.querycoord.load.latency.bucket': 'monotonic_count',
    'milvus.querycoord.load.req.count': 'monotonic_count',
    'milvus.querycoord.partition_num': 'gauge',
    'milvus.querycoord.querynode_num': 'gauge',
    'milvus.querycoord.release.latency.sum': 'monotonic_count',
    'milvus.querycoord.release.latency.count': 'monotonic_count',
    'milvus.querycoord.release.latency.bucket': 'monotonic_count',
    'milvus.querycoord.release.req.count': 'monotonic_count',
    'milvus.querycoord_task_num': 'gauge',
    'milvus.querynode.apply_bf_latency.sum': 'monotonic_count',
    'milvus.querynode.apply_bf_latency.count': 'monotonic_count',
    'milvus.querynode.apply_bf_latency.bucket': 'monotonic_count',
    'milvus.querynode.collection_num': 'gauge',
    'milvus.querynode.consume.bytes_counter.count': 'monotonic_count',
    'milvus.querynode.disk.cache.evict.bytes.count': 'monotonic_count',
    'milvus.querynode.disk.cache.evict.duration.count': 'monotonic_count',
    'milvus.querynode.disk.cache.evict.global_duration.sum': 'monotonic_count',
    'milvus.querynode.disk.cache.evict.global_duration.count': 'monotonic_count',
    'milvus.querynode.disk.cache.evict.global_duration.bucket': 'monotonic_count',
    'milvus.querynode.disk.cache.evict.count': 'monotonic_count',
    'milvus.querynode.disk.cache.load.bytes.count': 'monotonic_count',
    'milvus.querynode.disk.cache.load.duration.count': 'monotonic_count',
    'milvus.querynode.disk.cache.load.global_duration.sum': 'monotonic_count',
    'milvus.querynode.disk.cache.load.global_duration.count': 'monotonic_count',
    'milvus.querynode.disk.cache.load.global_duration.bucket': 'monotonic_count',
    'milvus.querynode.disk.cache.load.count': 'monotonic_count',
    'milvus.querynode.disk.used_size': 'gauge',
    'milvus.querynode.dml_vchannel_num': 'gauge',
    'milvus.querynode.execute_bytes_counter.count': 'monotonic_count',
    'milvus.querynode.flowgraph_num': 'gauge',
    'milvus.querynode.forward_delete_latency.sum': 'monotonic_count',
    'milvus.querynode.forward_delete_latency.count': 'monotonic_count',
    'milvus.querynode.forward_delete_latency.bucket': 'monotonic_count',
    'milvus.querynode.load.index_latency.sum': 'monotonic_count',
    'milvus.querynode.load.index_latency.count': 'monotonic_count',
    'milvus.querynode.load.index_latency.bucket': 'monotonic_count',
    'milvus.querynode.load.segment.concurrency': 'gauge',
    'milvus.querynode.load.segment.latency.sum': 'monotonic_count',
    'milvus.querynode.load.segment.latency.count': 'monotonic_count',
    'milvus.querynode.load.segment.latency.bucket': 'monotonic_count',
    'milvus.querynode.process_insert_or_delete_latency.sum': 'monotonic_count',
    'milvus.querynode.process_insert_or_delete_latency.count': 'monotonic_count',
    'milvus.querynode.process_insert_or_delete_latency.bucket': 'monotonic_count',
    'milvus.querynode.read_task.concurrency': 'gauge',
    'milvus.querynode.read_task.ready_len': 'gauge',
    'milvus.querynode.read_task.unsolved_len': 'gauge',
    'milvus.querynode.search.group.nq.sum': 'monotonic_count',
    'milvus.querynode.search.group.nq.count': 'monotonic_count',
    'milvus.querynode.search.group.nq.bucket': 'monotonic_count',
    'milvus.querynode.search.group.size.sum': 'monotonic_count',
    'milvus.querynode.search.group.size.count': 'monotonic_count',
    'milvus.querynode.search.group.size.bucket': 'monotonic_count',
    'milvus.querynode.search.group.topk.sum': 'monotonic_count',
    'milvus.querynode.search.group.topk.count': 'monotonic_count',
    'milvus.querynode.search.group.topk.bucket': 'monotonic_count',
    'milvus.querynode.search.nq.sum': 'monotonic_count',
    'milvus.querynode.search.nq.count': 'monotonic_count',
    'milvus.querynode.search.nq.bucket': 'monotonic_count',
    'milvus.querynode.search.topk.sum': 'monotonic_count',
    'milvus.querynode.search.topk.count': 'monotonic_count',
    'milvus.querynode.search.topk.bucket': 'monotonic_count',
    'milvus.querynode.segment.access.duration.count': 'monotonic_count',
    'milvus.querynode.segment.access.global_duration.sum': 'monotonic_count',
    'milvus.querynode.segment.access.global_duration.count': 'monotonic_count',
    'milvus.querynode.segment.access.global_duration.bucket': 'monotonic_count',
    'milvus.querynode.segment.access.count': 'monotonic_count',
    'milvus.querynode.segment.access.wait_cache.duration.count': 'monotonic_count',
    'milvus.querynode.segment.access.wait_cache.global_duration.sum': 'monotonic_count',
    'milvus.querynode.segment.access.wait_cache.global_duration.count': 'monotonic_count',
    'milvus.querynode.segment.access.wait_cache.global_duration.bucket': 'monotonic_count',
    'milvus.querynode.segment.access.wait_cache.count': 'monotonic_count',
    'milvus.querynode.segment.latency_per_vector.sum': 'monotonic_count',
    'milvus.querynode.segment.latency_per_vector.count': 'monotonic_count',
    'milvus.querynode.segment.latency_per_vector.bucket': 'monotonic_count',
    'milvus.querynode.sq.core_latency.sum': 'monotonic_count',
    'milvus.querynode.sq.core_latency.count': 'monotonic_count',
    'milvus.querynode.sq.core_latency.bucket': 'monotonic_count',
    'milvus.querynode.sq.queue.latency.sum': 'monotonic_count',
    'milvus.querynode.sq.queue.latency.count': 'monotonic_count',
    'milvus.querynode.sq.queue.latency.bucket': 'monotonic_count',
    'milvus.querynode.sq.queue.user_latency.sum': 'monotonic_count',
    'milvus.querynode.sq.queue.user_latency.count': 'monotonic_count',
    'milvus.querynode.sq.queue.user_latency.bucket': 'monotonic_count',
    'milvus.querynode.sq.reduce_latency.sum': 'monotonic_count',
    'milvus.querynode.sq.reduce_latency.count': 'monotonic_count',
    'milvus.querynode.sq.reduce_latency.bucket': 'monotonic_count',
    'milvus.querynode.sq.req.latency.sum': 'monotonic_count',
    'milvus.querynode.sq.req.latency.count': 'monotonic_count',
    'milvus.querynode.sq.req.latency.bucket': 'monotonic_count',
    'milvus.querynode.sq.segment_latency.sum': 'monotonic_count',
    'milvus.querynode.sq.segment_latency.count': 'monotonic_count',
    'milvus.querynode.sq.segment_latency.bucket': 'monotonic_count',
    'milvus.querynode.sq.wait_tsafe_latency.sum': 'monotonic_count',
    'milvus.querynode.sq.wait_tsafe_latency.count': 'monotonic_count',
    'milvus.querynode.sq.wait_tsafe_latency.bucket': 'monotonic_count',
    'milvus.querynode.wait_processing_msg': 'gauge',
    'milvus.querynode.watch_dml_channel_latency.sum': 'monotonic_count',
    'milvus.querynode.watch_dml_channel_latency.count': 'monotonic_count',
    'milvus.querynode.watch_dml_channel_latency.bucket': 'monotonic_count',
    'milvus.rootcoord.collection_num': 'gauge',
    'milvus.rootcoord.credential_num': 'gauge',
    'milvus.rootcoord.ddl_req.count': 'monotonic_count',
    'milvus.rootcoord.sync_timetick_latency.sum': 'monotonic_count',
    'milvus.rootcoord.sync_timetick_latency.bucket': 'monotonic_count',
    'milvus.rootcoord.sync_timetick_latency.count': 'monotonic_count',
    'milvus.rootcoord.ddl_req.latency.sum': 'monotonic_count',
    'milvus.rootcoord.ddl_req.latency.count': 'monotonic_count',
    'milvus.rootcoord.ddl_req.latency.bucket': 'monotonic_count',
    'milvus.rootcoord.ddl_req.latency_in_queue.sum': 'monotonic_count',
    'milvus.rootcoord.ddl_req.latency_in_queue.count': 'monotonic_count',
    'milvus.rootcoord.ddl_req.latency_in_queue.bucket': 'monotonic_count',
    'milvus.rootcoord.dml_channel_num': 'gauge',
    'milvus.rootcoord.entity_num': 'gauge',
    'milvus.rootcoord.force_deny_writing_counter.count': 'monotonic_count',
    'milvus.rootcoord.id_alloc.count': 'monotonic_count',
    'milvus.rootcoord.indexed_entity_num': 'gauge',
    'milvus.rootcoord.msgstream_obj_num': 'gauge',
    'milvus.rootcoord.num_of_roles': 'gauge',
    'milvus.rootcoord.partition_num': 'gauge',
    'milvus.rootcoord.produce_tt_lag_ms': 'gauge',
    'milvus.rootcoord.proxy_num': 'gauge',
    'milvus.rootcoord.qn_mem_high_water_level': 'gauge',
    'milvus.rootcoord.timestamp': 'gauge',
    'milvus.rootcoord.timestamp_saved': 'gauge',
    'milvus.runtime_info': 'gauge',
    'milvus.process.cpu_seconds.count': 'monotonic_count',
    'milvus.process.max_fds': 'gauge',
    'milvus.process.open_fds': 'gauge',
    'milvus.process.resident_memory_bytes': 'gauge',
    'milvus.process.start_time_seconds': 'gauge',
    'milvus.process.virtual_memory.bytes': 'gauge',
    'milvus.process.virtual_memory.max_bytes': 'gauge',
    'milvus.bf_search_cnt.sum': 'monotonic_count',
    'milvus.bf_search_cnt.count': 'monotonic_count',
    'milvus.bf_search_cnt.bucket': 'monotonic_count',
    'milvus.bitset_ratio.sum': 'monotonic_count',
    'milvus.bitset_ratio.count': 'monotonic_count',
    'milvus.bitset_ratio.bucket': 'monotonic_count',
    'milvus.build_latency.sum': 'monotonic_count',
    'milvus.build_latency.count': 'monotonic_count',
    'milvus.build_latency.bucket': 'monotonic_count',
    'milvus.cache_hit_cnt.sum': 'monotonic_count',
    'milvus.cache_hit_cnt.count': 'monotonic_count',
    'milvus.cache_hit_cnt.bucket': 'monotonic_count',
    'milvus.diskann_bitset_ratio.sum': 'monotonic_count',
    'milvus.diskann_bitset_ratio.count': 'monotonic_count',
    'milvus.diskann_bitset_ratio.bucket': 'monotonic_count',
    'milvus.diskann.range_search_iters.sum': 'monotonic_count',
    'milvus.diskann.range_search_iters.count': 'monotonic_count',
    'milvus.diskann.range_search_iters.bucket': 'monotonic_count',
    'milvus.diskann.search_hops.sum': 'monotonic_count',
    'milvus.diskann.search_hops.count': 'monotonic_count',
    'milvus.diskann.search_hops.bucket': 'monotonic_count',
    'milvus.exec_latency.sum': 'monotonic_count',
    'milvus.exec_latency.count': 'monotonic_count',
    'milvus.exec_latency.bucket': 'monotonic_count',
    'milvus.filter.connectivity_ratio.sum': 'monotonic_count',
    'milvus.filter.connectivity_ratio.count': 'monotonic_count',
    'milvus.filter.connectivity_ratio.bucket': 'monotonic_count',
    'milvus.filter.mv.activated_fields_cnt.sum': 'monotonic_count',
    'milvus.filter.mv.activated_fields_cnt.count': 'monotonic_count',
    'milvus.filter.mv.activated_fields_cnt.bucket': 'monotonic_count',
    'milvus.filter.mv.change_base_cnt.sum': 'monotonic_count',
    'milvus.filter.mv.change_base_cnt.count': 'monotonic_count',
    'milvus.filter.mv.change_base_cnt.bucket': 'monotonic_count',
    'milvus.filter.mv.only_cnt.sum': 'monotonic_count',
    'milvus.filter.mv.only_cnt.count': 'monotonic_count',
    'milvus.filter.mv.only_cnt.bucket': 'monotonic_count',
    'milvus.filter.mv.supplement_ep_bool_cnt.sum': 'monotonic_count',
    'milvus.filter.mv.supplement_ep_bool_cnt.count': 'monotonic_count',
    'milvus.filter.mv.supplement_ep_bool_cnt.bucket': 'monotonic_count',
    'milvus.graph_search_cnt.sum': 'monotonic_count',
    'milvus.graph_search_cnt.count': 'monotonic_count',
    'milvus.graph_search_cnt.bucket': 'monotonic_count',
    'milvus.hnsw.bitset_ratio.sum': 'monotonic_count',
    'milvus.hnsw.bitset_ratio.count': 'monotonic_count',
    'milvus.hnsw.bitset_ratio.bucket': 'monotonic_count',
    'milvus.hnsw.search_hops.sum': 'monotonic_count',
    'milvus.hnsw.search_hops.count': 'monotonic_count',
    'milvus.hnsw.search_hops.bucket': 'monotonic_count',
    'milvus.internal.core_search_latency.sum': 'monotonic_count',
    'milvus.internal.core_search_latency.count': 'monotonic_count',
    'milvus.internal.core_search_latency.bucket': 'monotonic_count',
    'milvus.internal.mmap.allocated_space_bytes.sum': 'monotonic_count',
    'milvus.internal.mmap.allocated_space_bytes.count': 'monotonic_count',
    'milvus.internal.mmap.allocated_space_bytes.bucket': 'monotonic_count',
    'milvus.internal.mmap.in_used_space_bytes': 'gauge',
    'milvus.internal.storage.kv_size.sum': 'monotonic_count',
    'milvus.internal.storage.kv_size.count': 'monotonic_count',
    'milvus.internal.storage.kv_size.bucket': 'monotonic_count',
    'milvus.internal.storage.load_duration.sum': 'monotonic_count',
    'milvus.internal.storage.load_duration.count': 'monotonic_count',
    'milvus.internal.storage.load_duration.bucket': 'monotonic_count',
    'milvus.internal.storage.op.count': 'monotonic_count',
    'milvus.internal.storage.request_latency.sum': 'monotonic_count',
    'milvus.internal.storage.request_latency.count': 'monotonic_count',
    'milvus.internal.storage.request_latency.bucket': 'monotonic_count',
    'milvus.io_cnt.sum': 'monotonic_count',
    'milvus.io_cnt.count': 'monotonic_count',
    'milvus.io_cnt.bucket': 'monotonic_count',
    'milvus.ivf_search_cnt.sum': 'monotonic_count',
    'milvus.ivf_search_cnt.count': 'monotonic_count',
    'milvus.ivf_search_cnt.bucket': 'monotonic_count',
    'milvus.load_latency.sum': 'monotonic_count',
    'milvus.load_latency.count': 'monotonic_count',
    'milvus.load_latency.bucket': 'monotonic_count',
    'milvus.quant.compute_cnt.sum': 'monotonic_count',
    'milvus.quant.compute_cnt.count': 'monotonic_count',
    'milvus.quant.compute_cnt.bucket': 'monotonic_count',
    'milvus.queue.latency.sum': 'monotonic_count',
    'milvus.queue.latency.count': 'monotonic_count',
    'milvus.queue.latency.bucket': 'monotonic_count',
    'milvus.range_search_latency.sum': 'monotonic_count',
    'milvus.range_search_latency.count': 'monotonic_count',
    'milvus.range_search_latency.bucket': 'monotonic_count',
    'milvus.raw_compute_cnt.sum': 'monotonic_count',
    'milvus.raw_compute_cnt.count': 'monotonic_count',
    'milvus.raw_compute_cnt.bucket': 'monotonic_count',
    'milvus.re_search_cnt.sum': 'monotonic_count',
    'milvus.re_search_cnt.count': 'monotonic_count',
    'milvus.re_search_cnt.bucket': 'monotonic_count',
    'milvus.search.latency.sum': 'monotonic_count',
    'milvus.search.latency.count': 'monotonic_count',
    'milvus.search.latency.bucket': 'monotonic_count',
    'milvus.search.topk.sum': 'monotonic_count',
    'milvus.search.topk.count': 'monotonic_count',
    'milvus.search.topk.bucket': 'monotonic_count',
}

OTHER_TEST_METRICS = {
    'milvus.datacoord.channel_checkpoint_unix_seconds': 'gauge',
    'milvus.datacoord.stored.binlog_size': 'gauge',
    'milvus.datacoord.stored.index_files_size': 'gauge',
    'milvus.datacoord.stored.rows_num': 'gauge',
    'milvus.datacoord.watched_dml_chanel_num': 'gauge',
    'milvus.datanode.consume.msg_count': 'count',
    'milvus.datanode.consume.tt_lag_ms': 'gauge',
    'milvus.datanode.msg.dispatcher_tt_lag_ms': 'gauge',
    'milvus.querycoord.current_target_checkpoint_unix_seconds': 'gauge',
    'milvus.querynode.consume.msg_count': 'count',
    'milvus.querynode.consume.tt_lag_ms': 'gauge',
    'milvus.querynode.entity.num': 'gauge',
    'milvus.querynode.entity.size': 'gauge',
    'milvus.querynode.msg_dispatcher_tt_lag_ms': 'gauge',
    'milvus.querynode.partition_num': 'gauge',
    'milvus.querynode.segment.num': 'gauge',
    'milvus.querynode.sq.req.count': 'monotonic_count',
    'milvus.rootcoord.sync_timetick_latency.bucket': 'count',
    'milvus.rootcoord.sync_timetick_latency.count': 'count',
    'milvus.rootcoord.timestamp': 'gauge',
    'milvus.storage.kv_size': 'gauge',
    'milvus.storage.op_count': 'count',
    'milvus.storage.request_latency': 'gauge',
}
