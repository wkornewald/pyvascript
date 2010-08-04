list = function(x) {
  var item, result;
  result = [];
  var _$tmp1_data = _$pyva_iter(x);
  var _$tmp2_len = _$tmp1_data.length;
  for (var _$tmp3_index = 0; _$tmp3_index < _$tmp2_len; _$tmp3_index++) {
    item = _$tmp1_data[_$tmp3_index];

    result.append(x);
  }

  return result;
}

tuple = function(x) {
  return list(x);
}

dict = function(x) {
  var key, result;
  result = {
    
  };
  var _$tmp4_data = _$pyva_iter(x);
  var _$tmp5_len = _$tmp4_data.length;
  for (var _$tmp6_index = 0; _$tmp6_index < _$tmp5_len; _$tmp6_index++) {
    key = _$tmp4_data[_$tmp6_index];

    result[key] = x[key];
  }

  return result;
}

int = function(x) {
  return parseInt(x);
}

float = function(x) {
  return parseFloat(x);
}

str = function(x) {
  return x.toString();
}

unicode = function(x) {
  return str(x);
}

if ((!Array.prototype.append)) {
  Array.prototype.append = Array.prototype.push;
}

if ((!Array.prototype.insert)) {
  Array.prototype.insert = function(index, item) {
    this.splice(index, 0, item);
  };
}

if ((!Array.prototype.extend)) {
  Array.prototype.extend = function(items) {
    var item;
    var _$tmp7_data = _$pyva_iter(items);
    var _$tmp8_len = _$tmp7_data.length;
    for (var _$tmp9_index = 0; _$tmp9_index < _$tmp8_len; _$tmp9_index++) {
      item = _$tmp7_data[_$tmp9_index];

      this.append(item);
    }

  };
}

if ((!Array.prototype.index)) {
  Array.prototype.index = Array.prototype.indexOf;
}

if ((!String.prototype.join)) {
  String.prototype.join = function(iterable) {
    return iterable.join(this);
  };
}

isinstance = function(item, cls) {
  var cls_item, isnumber;
  if (cls instanceof Array) {
    var _$tmp10_data = _$pyva_iter(cls);
    var _$tmp11_len = _$tmp10_data.length;
    for (var _$tmp12_index = 0; _$tmp12_index < _$tmp11_len; _$tmp12_index++) {
      cls_item = _$tmp10_data[_$tmp12_index];

      if (isinstance(item, cls_item)) {
        return true;
      }

    }

    return false;
  }

  if (((cls === tuple) || (cls === list))) {
    cls = Array;
  } else if ((cls === dict)) {
    cls = Object;
  } else if (((cls === str) || (cls === unicode))) {
    cls = String;
  } else if (((cls === int) || (cls === float))) {
    isnumber = (item.constructor === Number.prototype.constructor);
    return (isnumber && (cls(item) == item));
  } else {
    return item instanceof cls;
  }

  return (item.constructor === cls.prototype.constructor);
}

_$pyva_iter = function(iter_object) {
  var key_list;
  if ((isinstance(iter_object, list) || isinstance(iter_object, list))) {
    return iter_object;
  }

  key_list = [];
  for (var key in iter_object)
  key_list.append(key);
  return key_list;
}
