---
layout:     post
title:      "Jekyll + GitHub Page Blog Set Up"
subtitle:   " \"Set up Jekyll and GitHub on Mac\""
date:       2019-02-02 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Linux
    - Mac
---

## Jekyll

Jekyll 是一个简单的博客形态的静态站点生产机器。它有一个模版目录，其中包含原始文本格式的文档，通过一个转换器如 [Markdown](https://daringfireball.net/projects/markdown)和我们的[Liquid](https://github.com/Shopify/liquid/wiki)渲染器转化成一个完整的可发布的静态网站，你可以发布在任何你喜爱的服务器上。

#### 安装Jekyll

在安装Jekyll之前， 必须安装的环境：
 * Ruby
 * RubyGems
 * NodeJS或其他JavaScript运行环境
 * Python 2.7 及以上


使用RubyGems安装Jekyll:

`gem install jekyll`

如果要指定安装版本：

`gem install jekyll -v '指定版本号'`


#### 快速启动

```
# 安装bundler，bundler通过gemfile文件来管理gem包
gem install  bundler

# 创建一个新的Jekyll项目，并命名为myblog
jekyll new myblog

# 进入myblog目录
cd myblog

# 在Jekyll自带的服务器上预览你的项目，默认的运行地址为http://localhost:4000
# bundle exec 表示在当前项目依赖的上下文环境中执行命令 jekyll serve
bundle exec jekyll serve
```

#### 基本用法

```
$ jekyll build
# => 当前文件夹中的内容将会生成到 ./_site 文件夹中。

$ jekyll build --destination <destination>
# => 当前文件夹中的内容将会生成到目标文件夹<destination>中。

$ jekyll build --source <source> --destination <destination>
# => 指定源文件夹<source>中的内容将会生成到目标文件夹<destination>中。

$ jekyll build --watch
# => 当前文件夹中的内容将会生成到 ./_site 文件夹中，
#    查看改变，并且自动再生成。
```

Jekyll 自带开发用的Server:

```
jekyll serve
# 开发服务器将会运行在 http://localhost:4000/
```

#### 目录结构

```
├── 404.html
├── Gemfile
├── Gemfile.lock
├── _config.yml
├── _posts
│   └── 2018-03-31-welcome-to-jekyll.markdown
├── about.md
├── index.html
└── posts.html
```

![image](/img/in-post/post-jekyll-structure.png)
