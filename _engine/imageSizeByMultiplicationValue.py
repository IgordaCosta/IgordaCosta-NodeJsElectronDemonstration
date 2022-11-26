
# InitialValue=7.9

def imageSizeByMultiplicationValue(MultiplicationValue):

    ReferenceValueW=1700
    ReferenceValueH=2200

    dpi=96

    multiplicationFactor=ReferenceValueH/ReferenceValueW



    Imagewidth=int(MultiplicationValue*dpi)

    Imageheight=int(multiplicationFactor*Imagewidth)

    return Imagewidth, Imageheight