import tkinter as tk

#----------------計算ボタンを押したときの処理----------------#
def calc():
    #計算の準備
    h_meter = float(textHeight.get()) / 100
    w_kg = float(textWeight.get())
    w_kg_fatnow = w_kg * float(txt_bodyfat.get()) / 100
    w_kg_idealfat = w_kg * float(txt_bodyfatgoal.get()) / 100

    #除脂肪体重を表示
    w_kg_nofat = w_kg - w_kg_fatnow
    result_weightnofat = "除脂肪体重:{0}kg".format(w_kg_nofat)
    lbl_weightnofat['text'] = result_weightnofat
    
    #目標体重を表示
    w_kg_goal = w_kg + w_kg_idealfat - w_kg_fatnow
    result_weightgoal = "目標体重:{0}kg".format(w_kg_goal)
    lbl_weightgoal['text'] = result_weightgoal

    #現在のBMIを表示
    bmi = w_kg / h_meter ** 2
    result_bminow = "現在のBMI:{0}".format(bmi)
    lbl_bminow['text'] = result_bminow

    #目標BMIを表示
    idealbmi = w_kg_goal / h_meter ** 2
    result_bminow = "目標のBMI:{0}".format(idealbmi)
    lbl_bmigoal['text'] = result_bminow

#----------------ウィンドウを作成----------------#
root = tk.Tk()
root.title("理想の体重計算（体脂肪率を考慮）")
root.geometry("300x350")

#身長のラベル
lbl_Height = tk.Label(root, text=u'身長(cm):')
lbl_Height.pack()
#身長のテキスト
textHeight = tk.Entry(root)
textHeight.insert(tk.END, '170')
textHeight.pack()

#現在の体重のラベル
lbl_Weight = tk.Label(root, text=u'現在の体重(kg):')
lbl_Weight.pack()
#現在の体重のテキスト
textWeight = tk.Entry(root)
textWeight.insert(tk.END, '70')
textWeight.pack()

#体脂肪率のラベル
lbl_bodyfat = tk.Label(root, text=u'現在の体脂肪率(%):')
lbl_bodyfat.pack()
#体脂肪率のテキスト
txt_bodyfat = tk.Entry(root)
txt_bodyfat.insert(tk.END, '14')
txt_bodyfat.pack()

#目標の体脂肪率のラベル
lbl_bodyfatgoal = tk.Label(root, text=u'目標体脂肪散率(%):')
lbl_bodyfatgoal.pack()
#目標の体脂肪率のテキスト
txt_bodyfatgoal = tk.Entry(root)
txt_bodyfatgoal.insert(tk.END, '9')
txt_bodyfatgoal.pack()

#----------------計算結果の表示----------------#
#除脂肪体重を表示
lbl_weightnofat = tk.Label(root, text=u'除脂肪体重:')
lbl_weightnofat.pack()
#目標体重を表示
lbl_weightgoal = tk.Label(root, text=u'目標体重:')
lbl_weightgoal.pack()
#現在のBMIを表示
lbl_bminow = tk.Label(root, text=u'現在のBMI:')
lbl_bminow.pack()
#目標のBMIを表示
lbl_bmigoal = tk.Label(root, text=u'目標のBMI:')
lbl_bmigoal.pack()

#-----------------計算処理開始-----------------#
calcButton = tk.Button(root, text=u'計算')
calcButton["command"] = calc
calcButton.pack()

#ここから上の処理を繰り返す
root.mainloop()