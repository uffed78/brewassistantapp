
from flask import Blueprint

bp = Blueprint('brewfather', __name__)

@bp.route('/sync-inventory', methods=['POST'])
def sync_inventory():
    # Logic for syncing with Brewfather API
    return {"message": "Inventory synced successfully"}
