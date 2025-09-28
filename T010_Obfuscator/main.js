
const fs = require('fs');
const path = require('path');
const JavaScriptObfuscator = require('javascript-obfuscator');

try{
    const inputPath = path.join(__dirname, 'input.js');
    const outputPath = path.join(__dirname, 'output.js');

    const code = fs.readFileSync(inputPath, 'utf-8');
    const obfuscated = JavaScriptObfuscator.obfuscate(code, {
        compact: false,                         // 不压缩代码，方便调试
        controlFlowFlattening: true,            // 启用控制流扁平化
        controlFlowFlatteningThreshold: 1,      // 100% 概率应用控制流扁平化
        stringArray: true,                      // 启用字符串抽取
        stringArrayEncoding: ['base64'],        // 必须是数组，支持 'base64' / 'rc4' / 'none'
        stringArrayThreshold: 1                 // 100% 概率抽取字符串
    });
    fs.writeFileSync(outputPath, obfuscated.getObfuscatedCode(), 'utf-8');
    console.log('混淆完成，输出文件：', outputPath);
}catch (e) {
    console.error('混淆失败：', e.message)
}
