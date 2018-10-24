#! python
import subprocess

def go(dothis):
    print(dothis)
    return subprocess.getoutput(dothis)

#Files=["abstract-algebra", "analysis", "topology", "category-theory"]
Files=["category-theory"]

[go("pdflatex "+i) for i in Files]

Ftex=[i + ".tex" for i in Files]
Count=go("egrep '(\\Dcard|\\Card|begin.flashcard)' " + " ".join(Ftex)  + " | wc -l")
print(str(Count)+" cards.")
go("rm counts; for i in `seq 1 2 " + Count + "`; do echo $i >> counts; done")
Pages=go("shuf counts | awk '{print $1 \",\" $1+1}'| tr '\n' ','|sed 's/,$//'")

go("pdfjam --trim '0in 9.5in 5in 1in' " + "  ".join([" "+i +".pdf " for i in Files]) + " -o mid1.pdf")
go("pdfjam mid1.pdf \"" + Pages + "\" --no-tidy -o mid.pdf")
go("pdfcrop --clip mid.pdf cards.pdf")


print (Count)

