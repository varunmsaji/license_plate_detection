def get_car(licence_plate,track_id):
    return [0,0,0,0,0]





def get_license(thresholdsss):
    return 0,0


def write_csv(results, output_path):
    """
    Write the results to a CSV file.

    Args:
        results (dict): Dictionary containing the results.
        output_path (str): Path to the output CSV file.
    """
    with open(output_path, 'w') as f:
        f.write('{},{},{},{},{},{},{}\n'.format('frame_nmr', 'car_id', 'car_bbox',
                                                'license_plate_bbox', 'license_plate_bbox_score', 'license_number',
                                                'license_number_score'))

        for frame_nmr in results.keys():
            for car_id in results[frame_nmr].keys():
                print(results[frame_nmr][car_id])
                if 'car' in results[frame_nmr][car_id].keys() and \
                   'license_plate' in results[frame_nmr][car_id].keys() and \
                   'text' in results[frame_nmr][car_id]['license_plate'].keys():
                    f.write('{},{},{},{},{},{},{}\n'.format(frame_nmr,
                                                            car_id,
                                                            '[{} {} {} {}]'.format(
                                                                results[frame_nmr][car_id]['car']['bbox'][0],
                                                                results[frame_nmr][car_id]['car']['bbox'][1],
                                                                results[frame_nmr][car_id]['car']['bbox'][2],
                                                                results[frame_nmr][car_id]['car']['bbox'][3]),
                                                            '[{} {} {} {}]'.format(
                                                                results[frame_nmr][car_id]['license_plate']['bbox'][0],
                                                                results[frame_nmr][car_id]['license_plate']['bbox'][1],
                                                                results[frame_nmr][car_id]['license_plate']['bbox'][2],
                                                                results[frame_nmr][car_id]['license_plate']['bbox'][3]),
                                                            results[frame_nmr][car_id]['license_plate']['bbox_score'],
                                                            results[frame_nmr][car_id]['license_plate']['text'],
                                                            results[frame_nmr][car_id]['license_plate']['text_score'])
                            )
        f.close()


def new_write(results, output_path):
    """
    Write the results to a CSV file.

    Args:
        results (dict): Dictionary containing the results.
        output_path (str): Path to the output CSV file.
    """
    try:
        with open(output_path, 'w') as f:
            f.write('frame_nmr,car_id,car_bbox,license_plate_bbox,license_plate_bbox_score,license_number,license_number_score\n')

            for frame_nmr, frame_results in results.items():
                print("Frame Number:", frame_nmr)
                for car_id, car_data in frame_results.items():
                    print("Car ID:", car_id)
                    print("Car Data:", car_data)
                    if 'car' in car_data and 'license_plate' in car_data and 'text' in car_data['license_plate']:
                        car_bbox = ' '.join(map(str, car_data['car']['bbox']))
                        plate_bbox = ' '.join(map(str, car_data['license_plate']['bbox']))
                        plate_bbox_score = car_data['license_plate']['bbox_score']
                        plate_text = car_data['license_plate']['text']
                        plate_text_score = car_data['license_plate']['text_score']
                        print("the data to write",frame_nmr,car_id,car_bbox,plate_bbox,plate_bbox_score,plate_text,plate_text_score)

                        f.write(f"{frame_nmr},{car_id},{car_bbox},{plate_bbox},{plate_bbox_score},{plate_text},{plate_text_score}\n")
    except Exception as e:
        print("An error occurred:", e)

