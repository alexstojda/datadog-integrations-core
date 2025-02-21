# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>


def instance_add_node_tag_to_events():
    return True


def instance_collections_indexes_stats():
    return False


def instance_connection_scheme():
    return 'mongodb'


def instance_database_instance_collection_interval():
    return False


def instance_dbm():
    return False


def instance_dbstats_tag_dbname():
    return True


def instance_disable_generic_tags():
    return False


def instance_empty_default_hostname():
    return False


def instance_min_collection_interval():
    return 15


def instance_replica_check():
    return True


def instance_timeout():
    return 30


def instance_tls():
    return False


def instance_tls_allow_invalid_certificates():
    return False


def instance_tls_allow_invalid_hostnames():
    return False
