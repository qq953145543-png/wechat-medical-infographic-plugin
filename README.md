# 公众号医学科普系列长图（Codex 插件）

输入一个健康科普系列主题，自动完成：

1. 策划 5 个递进的患者问题标题；
2. 增加第 6 张“该做／不该做”清单；
3. 核对医学事实；
4. 生成 6 张人物、版式与配色统一的微信公众号竖版长图；
5. 检查中文、数字、单位和医学安全。

## 在 Codex 中安装

第一次使用时，在 Codex 终端依次运行：

```bash
codex plugin marketplace add qq953145543-png/wechat-medical-infographic-plugin
codex plugin add wechat-medical-infographic@wechat-medical-infographic
```

安装完成后，新建一个 Codex 任务，输入：

```text
使用 $artifact-template-wechat，主题：高血压健康知识大全
```

Codex 会先列出 01–06 的标题，然后继续生成六张系列图片。

## 更新

发布新版本后，重新运行：

```bash
codex plugin marketplace add qq953145543-png/wechat-medical-infographic-plugin
codex plugin add wechat-medical-infographic@wechat-medical-infographic
```

随后新建任务使用更新后的版本。

## 使用要求

- 安装 Codex，并登录可使用图片生成的账号；
- 保持联网，以便核对最新医学资料；
- 医学科普内容不能代替医生的个体化诊断与治疗建议。

## 包含内容

- 完整的六图生成工作流；
- 两张视觉参考图；
- 固定人物、配色、版式与信息卡规范；
- 医学安全和中文校对规则。
