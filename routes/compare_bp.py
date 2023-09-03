from flask import Blueprint

from controllers.compareController import ItemController


class ItemBlueprint:
    item_bp = Blueprint('item_bp', __name__, url_prefix='/item')
    item_bp.route('/item',methods=['POST'])(ItemController.items)