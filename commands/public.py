from __future__ import print_function
import sys
import json
import logging
from shared.common import parse_arguments
from shared.public import get_public_nodes

__description__ = "Find publicly exposed services and their ports"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def public(accounts, config):
    all_accounts = []

    for account in accounts:
        logger.info(f'Calling get_pulic_nodes on {account} with config {config}')
        public_nodes, warnings = get_public_nodes(account, config)
        for public_node in public_nodes:
            logger.info(f'Appending public_node: {public_node}')
            all_accounts.append(public_node)
        for warning in warnings:
            print("WARNING: {}".format(warning), file=sys.stderr)
    
    print(json.dumps(all_accounts, indent=4, sort_keys=True))


def run(arguments):
    _, accounts, config = parse_arguments(arguments)
    logger.info('Calling public(accounts, config)')
    public(accounts, config)
