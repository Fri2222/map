window._AMapSecurityConfig = {
  securityJsCode: 'a4f7e62534bbc0a8b6dbf252fd0e1a4f',
};

AMapLoader.load({
  key: "b03c0fabcb3089acd1b047c5c6e29181",
  version: "2.0", // 指定要加载的 JS API 的版本，缺省时默认为 1.4.15
})
.then((AMap) => {
  // JS API 加载完成后获取AMap对象
  const map = new AMap.Map("container", {
    viewMode: '2D', // 默认使用 2D 模式
    zoom: 11, // 地图级别
    center: [116.397428, 39.90923], // 地图中心点
  });
})
.catch((e) => {
  console.error(e); // 加载错误提示
});
