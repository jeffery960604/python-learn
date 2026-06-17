# 程式運作流程圖：繼承與 super() 說明

## 類別繼承關係圖

```mermaid
classDiagram
    class vehicle {
        +brand
        +__init__(brand)
        +move()
    }

    class airplane {
        +brand (繼承自 vehicle)
        +wingSpan
        +__init__(brand, wingSpan)
        +move() (繼承自 vehicle，未覆寫)
        +fly()
    }

    vehicle <|-- airplane : 繼承 (Inheritance)
```

---

## 程式執行流程（當你執行 `test = airplane("姆芋", 132)`）

```mermaid
flowchart TD
    A["🚀 開始執行\ntest = airplane('姆芋', 132)"] --> B

    B["airplane.__init__(brand='姆芋', wingSpan=132) 被呼叫"]
    B --> C

    C["遇到 super().__init__(brand)\n👆 叫老爸 vehicle 出來幫忙"]
    C --> D

    D["vehicle.__init__(brand='姆芋') 執行\n✅ self.brand = '姆芋'"]
    D --> E

    E["回到 airplane.__init__\n✅ self.wingSpan = 132"]
    E --> F

    F["🏭 工廠完成！test 這台飛機被打造出來\ntest.brand = '姆芋'\ntest.wingSpan = 132"]

    F --> G["test.move() 被呼叫"]
    G --> H{"airplane 有沒有\n自己的 move()？"}
    H -- "❌ 沒有" --> I["往上找老爸 vehicle 的 move()"]
    I --> J["✅ 印出：姆芋正在移動"]

    F --> K["test.fly() 被呼叫"]
    K --> L{"airplane 有沒有\n自己的 fly()？"}
    L -- "✅ 有！" --> M["執行 airplane 自己的 fly()"]
    M --> N["✅ 印出：姆芋正在高空飛行"]
```

---

## 覆寫（Override）的運作邏輯

```mermaid
flowchart TD
    P["假設打造 RocketShip 物件\nrocket.move() 被呼叫"] --> Q

    Q{"RocketShip 有沒有\n自己的 move()？"}
    Q -- "✅ 有！（覆寫過）" --> R["直接執行 RocketShip.move()\n老爸的 move() 被蓋掉了！"]
    R --> S["印出：SpaceX 點火發射！🚀"]

    Q -- "❌ 沒有" --> T["往上找老爸的 move()"]
    T --> U["印出：SpaceX 正在移動..."]
```

---

## super() 的加料覆寫（ElectricPlane 示範）

```mermaid
flowchart TD
    V["electric.move() 被呼叫"] --> W

    W["ElectricPlane.move() 執行\n第一行：super().move()"]
    W --> X["叫老爸 vehicle.move() 先跑\n印出：空中巴士 正在移動..."]
    X --> Y["回到 ElectricPlane.move()\n繼續執行第二行"]
    Y --> Z["印出：電池續航 3000 公里，零排放飛行中 🌿"]
```

> **總結規則**：
> - Python 呼叫方法時，**先在兒子身上找**，找到就用兒子的。
> - 找不到，才**往上爬，去老爸那裡找**。
> - `super()` 就是「手動叫老爸出來」的魔法鑰匙。
