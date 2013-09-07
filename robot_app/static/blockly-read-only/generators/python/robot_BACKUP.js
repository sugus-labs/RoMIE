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
  var code = 'turn_left()\n'
  return code;
};

Blockly.Python.robot_wall = function() {
  var code = 'sensor_wall() '
  return code;
};

Blockly.Python.robot_if = function() {
  var statements_do = Blockly.Python.statementToCode(this, 'do');
  // TODO: Assemble Python into code variable.
  var code = 'if sensor_wall():\n' + statements_do
  return code;
};
