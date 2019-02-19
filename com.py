import boto3

if __name__ == "__main__":

    sourceFile='/home/abhay/Downloads/IMG_20180830_214156600 (1).jpg'
    targetFile='/home/abhay/Downloads/42434847_112617176285533_70605787704480982_n.jpg'
    client=boto3.client('rekognition')
   
    imageSource=open(sourceFile,'rb')
    imageTarget=open(targetFile,'rb')

    response=client.compare_faces(SimilarityThreshold=70,
                                  SourceImage={'Bytes': imageSource.read()},
                                  TargetImage={'Bytes': imageTarget.read()})
    
    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = str(faceMatch['Similarity'])
        print('The faces at ' +
               str(position['Left']) + ' and ' +
               str(position['Top']) +
               ' matches with ' + similarity + '% confidence')

    imageSource.close()
    imageTarget.close()               
