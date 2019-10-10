def formatMoney(value_to_parse):
        try:
            rounded = round(float(value_to_parse),2)
            # split to get decimal + integer
            parsed_value = '{:,}'.format(rounded).replace(',', ' ')
            # decide if need to add extra 0
            if len(parsed_value.split('.')[1]) == 1:
                return f"{parsed_value}0"
            return parsed_value
        except ValueError:
            print(f"could not convert to float: '{value_to_parse}'")
            return ""
        except:
            print(f"unexpected error: '{value_to_parse}'")
            return ""
