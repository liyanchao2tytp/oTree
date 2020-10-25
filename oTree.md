# oTree开发文档

使用otree开发了一个调查测试的小项目。一共分为四个app，两个调查问卷，一个公共物品实验，一个信任实验。



## 开发中遇到的问题

### 引入element ui问题

element ui中的表格是通过data数据出来的，但是我们需要在每行的最后一格 放入一个不同的由后台生成的input标签。

我在官方文档的例子中找到了



```html
    <template slot-scope="scope">
        <el-button
          size="mini"
          @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)">删除</el-button>
      </template>
```



我觉得可以在template标签中放入{{   formfield player.q1  }} ， 但是无法遍历出q1-q10，所生成的十个input全是player.q1。



**解决方法** ：

​				在页面中使用js修改生成的input的属性值和label的属性值



```js
    var button = document.getElementsByClassName("el-table__row")
    for(let i=0;i<button.length;i++){
        let inputs=button[i].getElementsByTagName("input")
        let labels = button[i].getElementsByTagName('label')
        
        for(let j=0;j<inputs.length;j++){
            let num=i+1
        {# 修改Input标签中的属性 #}{#  修改label标签的属性  #}
            inputs[j].setAttribute("name","q"+num)
            if(j%2==0){
                inputs[j].setAttribute('id',`id_q${num}_0`)
                labels[j].setAttribute('for',`id_q${num}_0`)
            }else{
                inputs[j].setAttribute('id',`id_q${num}_1`)
                labels[j].setAttribute('for',`id_q${num}_1`)
            }
        }
    }
```



## 信任实验

信任实验在otree创建项目的时候会默认给你个例子。但这个例子只是在两个player之间进行send和sendback。

但是我们项目要求是三个人之间进行send和sendback。所以是三个人一组。