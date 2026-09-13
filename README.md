# 公众号医学科普系列长图 Skill

输入一个健康科普系列主题，自动完成：

1. 策划 5 个递进的患者问题标题；
2. 增加第 6 张“该做／不该做”清单；
3. 核对医学事实；
4. 生成 6 张人物、版式与配色统一的微信公众号竖版长图；
5. 每张图生成后自动撰写约 300 字配套文案；
6. 整理为完整公众号文章，并可一键导入公众号草稿箱；
7. 检查中文、数字、单位和医学安全。

## 在 Codex 对话中安装

不需要打开终端。学员在 Codex 中新建一个任务，把下面整段话复制进去发送：

```text
请使用 $skill-installer 安装以下两个最新版 Skills：

https://github.com/qq953145543-png/wechat-medical-infographic-plugin/tree/main/artifact-template-wechat

https://github.com/JimLiu/baoyu-skills/tree/main/skills/baoyu-post-to-wechat

这是首次安装，不要使用旧的本地缓存。安装完成后告诉我安装结果。
```

Codex 完成安装后，再新建一个任务并输入：

```text
$artifact-template-wechat 高血压健康知识大全
```

需要生成后直接导入公众号草稿，可输入：

```text
$artifact-template-wechat 高血压健康知识大全，完成后为每张图生成约300字文案，并一键导入公众号草稿
```

主题可以替换为糖尿病日常管理、冠心病健康知识、骨质疏松预防等。

Codex 会先列出 01–06 的系列标题，再生成六张统一风格的图片和六段配套文案，并整理成公众号文章。

首次导入公众号时，Codex 会打开浏览器，学员需要使用管理员微信扫码登录公众号。默认只保存到草稿箱，不会直接群发。

## 使用要求

- 使用支持 Skills 与图片生成的 Codex 桌面应用；
- 登录可使用图片生成的账号；
- 保持联网，以便安装 Skill 和核对最新医学资料；
- 医学科普内容不能代替医生的个体化诊断与治疗建议。

## 包含内容

- 完整的六图生成工作流；
- 两张视觉参考图；
- 固定人物、配色、版式与信息卡规范；
- 医学安全和中文校对规则。
- 每图约 300 字的公众号配套文案；
- 六图六文整理与公众号草稿导入流程。


---

## 医学文章一键成稿、配图与微信预览

新版 `$wechat-medical-oneclick` 会核对权威医学资料、撰写和格式化文章、一次性生成全部 6～8 张统一人物配图，并制作图片内嵌的微信公众号本地预览。

学员不需要下载压缩包或打开终端，直接在 Codex 中发送：

```text
请使用 $skill-installer 从 GitHub 安装以下最新版 Skills：

https://github.com/qq953145543-png/wechat-medical-infographic-plugin/tree/main/wechat-medical-oneclick

https://github.com/JimLiu/baoyu-skills/tree/main/skills/baoyu-format-markdown

https://github.com/JimLiu/baoyu-skills/tree/main/skills/baoyu-article-illustrator

https://github.com/JimLiu/baoyu-skills/tree/main/skills/baoyu-post-to-wechat

这是首次安装。请直接完成下载和安装，不要只给我安装教程。安装完成后逐项报告结果，并提醒我重新打开一个 Codex 任务使用 $wechat-medical-oneclick。
```

固定女性医护角色参考图已经随技能打包，首次运行会自动还原，不需要学员再次上传。
