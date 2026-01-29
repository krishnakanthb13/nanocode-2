#!/usr/bin/env node

const { spawn } = require('child_process');
const path = require('path');

// Get the directory where launcher.py is located
const projectRoot = path.join(__dirname, '..');

// Command to run the python launcher
const child = spawn('python', ['launcher.py'], {
    cwd: projectRoot,
    stdio: 'inherit',
    shell: true
});

child.on('exit', (code) => {
    process.exit(code);
});
