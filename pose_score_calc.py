annotations = [
    {
        "keypoints": [
            360.18, 299.65, 1.0, 364.04, 294.79, 0.96, 355.07, 295.04, 0.98, 369.58, 297.13, 0.83, 347.77, 298.04, 0.94, 381.79, 317.4, 0.94, 341.23, 321.81, 0.95, 387.61, 341.62, 0.62, 335.08, 350.91, 0.96, 373.34, 356.88, 0.44, 335.82, 363.87, 0.9, 373.8, 362.83, 0.86, 350.46, 364.86, 0.96, 388.86, 361.72, 0.66, 328.08, 374.7, 0.69, 338.47, 381.58, 0.34, 0.0, -3.0, 0.0
        ],
        "bbox": [
            321.09, 292.01, 74.9, 96.17
        ],
        "score": 0.821,
        "category_id": 1
    },
    {
        "keypoints": [ 81.04, 316.39, 0.8, 84.85, 313.13, 0.88, 79.19, 312.31, 0.67, 99.87, 308.71, 0.96, 0.0, -3.0, 0.0, 121.95, 317.08, 1.0, 78.87, 322.75, 0.98, 145.26, 347.63, 0.99, 59.34, 349.75, 0.96, 125.94, 353.11, 0.96, 52.33, 381.5, 0.97, 121.69, 359.37, 0.97, 95.56, 363.15, 0.97, 152.58, 360.37, 0.91, 72.03, 367.25, 0.88, 0.0, -3.0, 0.0, 0.0, -3.0, 0.0
        ],
        "bbox": [
            45.13, 305.11, 116.65, 83.59
        ],
        "score": 0.819,
        "category_id": 1

    },
    {
        "keypoints": [
            0.0, -3.0, 0.0, 0.0, -3.0, 0.0, 0.0, -3.0, 0.0, 388.01, 149.0, 1.0, 410.68, 149.9, 0.95, 376.6, 177.27, 0.98, 425.45, 178.19, 0.98, 337.24, 190.82, 0.98, 463.56, 192.09, 0.98, 301.44, 193.76, 0.98, 495.15, 185.29, 0.97, 389.34, 251.83, 0.97, 414.38, 251.49, 0.98, 384.25, 315.64, 0.82, 409.22, 317.9, 0.96, 0.0, -3.0, 0.0, 405.56, 367.51, 0.66
        ],
        "bbox": [
            289.84, 142.48, 216.49, 234.07
        ],
        "score": 0.788,
        "category_id": 1
    },
    {
        "keypoints": [
            239.69, 318.88, 0.48, 0.0, -3.0, 0.0, 235.94, 316.98, 0.68, 0.0, -3.0, 0.0, 222.3, 314.72, 0.84, 241.28, 320.26, 0.93, 201.98, 316.96, 1.0, 241.98, 351.26, 0.83, 197.04, 349.91, 0.78, 240.17, 378.14, 0.77, 195.31, 375.14, 0.67, 222.78, 339.59, 0.61, 199.07, 340.1, 0.58, 222.55, 374.28, 0.42, 0.0, -3.0, 0.0, 0.0, -3.0, 0.0, 0.0, -3.0, 0.0
        ],
        "bbox": [
            190.44, 312.1, 56.65, 70.61
        ],
        "score": 0.614,
        "category_id": 1
    },
    {
        "keypoints": [
            493.12, 349.29, 0.61, 494.84, 345.06, 0.55, 488.95, 346.07, 0.53, 503.2, 333.74, 0.44, 0.0, -3.0, 0.0, 522.08, 331.19, 0.76, 492.33, 334.51, 0.55, 549.21, 351.31, 0.65, 0.0, -3.0, 0.0, 0.0, -3.0, 0.0, 0.0, -3.0, 0.0, 542.72, 344.51, 0.86, 523.54, 346.43, 1.0, 522.31, 377.06, 0.81, 501.11, 378.52, 0.88, 566.24, 384.99, 0.62, 0.0, -3.0, 0.0
        ],
        "bbox": [
            486.3, 325.06, 87.45, 67.44
        ],
        "score": 0.597,
        "category_id": 1
    }
]

pose_scores = []
for annot in annotations:
    pose_score = 0
    kpt_scores = annot['keypoints'][2::3]
    # sort keypoint confidence scores in descending order
    sorted_kpt_scores = sorted(kpt_scores, reverse=True)
    # calculate pose score
    for i_score, score in enumerate(sorted_kpt_scores):
        print(i_score, score)
        # 3 most probable keypoints contribute three times more to pose score than other keypoints
        if i_score < 3:
            pose_score += 3 * score
        else:
            pose_score += score

    # divide accumulated keypoint scores by number of keypoints
    # add 6 for additionally weighted 3 most probable keypoints
    pose_score /= (17. + 3 * 2.)
    annot['calculated_score'] = pose_score


for ind, annot in enumerate(annotations):
    print('annotation #', ind)
    print('Given score', annot['score'])
    print('Calculated score score', annot['calculated_score'])
