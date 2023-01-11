import MetaTrader5
if not MetaTrader5.initialize():
    print("initialize() failed, error code =",MetaTrader5.last_error())
    quit()

# request = {'action': MetaTrader5.TRADE_ACTION_DEAL, 
# 'symbol': 'ENQZ22', 
# 'volume': 1.0, 
# 'type': MetaTrader5.ORDER_TYPE_BUY, 
# 'sl': MetaTrader5.symbol_info("ENQZ22").ask - (float(int((2.82546*2.5)/0.25))*0.25), 
# 'tp': MetaTrader5.symbol_info("ENQZ22").ask + (float(int(((2.82546*2.5)*2)/0.25))*0.25), 
# 'type_filling': 2, 
# 'type_time': 0, 
# 'comment': 'Green Order'}

# order_result = MetaTrader5.order_send(request)
# # Notify based on return outcomes
# if order_result[0] == 10009:
#     print(f"Order for ENQZ22 successful")
# else:
#     print(f"Error placing order. ErrorCode {order_result[0]}, Error Details: {order_result}")
# print(MetaTrader5.symbol_info("ENQZ22").ask)
# print(request)
# print(MetaTrader5.symbol_info("ENQZ22").point)
def get_open_positions():
    # Get position objects
    positions = MetaTrader5.positions_get()
    # Return position objects
    return positions
print(get_open_positions()[0])