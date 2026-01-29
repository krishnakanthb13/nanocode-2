#!/usr/bin/env node

const { spawn } = require('child_process');
const path = require('path');

// Get the directory where launcher.py is located
const projectRoot = path.join(__dirname, '..');
const launcherPath = path.join(projectRoot, 'launcher.py');

// Command to run the python launcher from the current directory
const child = spawn('python', [launcherPath], {
    stdio: 'inherit',
    shell: true
});

child.on('exit', (code) => {
    process.exit(code);
});
