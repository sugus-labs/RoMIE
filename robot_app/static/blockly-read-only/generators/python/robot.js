Blockly.Python = Blockly.Generator.get('Python');

Blockly.Python.robot_forward = function() {
  var code = 'forward()\n'
  return code;
};

Blockly.Python.robot_turn_right = function() {
  var code = 'turn_right()\n'
  return code;
};

Blockly.Python.robot_turn_left = function() {
  var code = 'turn_left()\n';
  return code;
};

Blockly.Python.robot_wall = function() {
  var code = 'sensor_wall()'
  return code;
};

Blockly.Python.robot_if = function() {
  // If/elseif/else condition.
  var branch = Blockly.Python.statementToCode(this, 'DO') || '  pass\n';
  var code = 'if sensor_wall():\n' + branch;
  if (this.elseCount_) {
    branch = Blockly.Python.statementToCode(this, 'ELSE') || '  pass\n';
    code += 'else:\n' + branch;
  }
  return code;
};
