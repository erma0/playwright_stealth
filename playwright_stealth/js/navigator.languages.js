Object.defineProperty(Object.getPrototypeOf(navigator), 'languages', {
    get: () => opts.languages || ['zh-CN', 'zh']
})
