import base64


def bin_decode(bin_string):
    normal_str = ""
    for i in range((len(bin_string) // 8)):
        normal_str += chr(int(bin_string[8 * i:8 * (i + 1)], 2))
    return normal_str


input_string = "VmtaV1UxSnRVWGROVmxaU1YwZG9UMVpyVmxkTk1WSlhWV3RhYTAxRVJsWlZWbWhyVkd4S1JsSnFVbFZXYkVwRFdrUkJlRkpXUmxs" \
               "aFJUVlRVbFpaTUZaR1dsTlJiVlpHVFZWV1VsZEhVazlXYTFaSFRURlNWbFZyU210TlJFWldWVlpvYjFSc1drWlNhazVWVmxaS1Ix" \
               "cEVRWGhTVmtwWllVVTFVMUpXV1RCV1JscFRVbTFSZDAxV1ZsTlhSMmhQVld0V1YwMHhVbGRWYTBwc1VsUkdWbFZzYUd0VWJGcEdV" \
               "bXBPVlZaV1NrZGFSRUY0VWxaR1dWcEZOVmRTVmxsNlZrWmFVMUp0VVhkTlZsWlRWMGRvVDFaclZrZE9SbEpYVld0S2EwMUVSbFpW" \
               "Vm1oclZHeEtSbFpxVWxWV1ZrcEhXa1JCZUZKV1NsbGFSVFZYVWxaWmVsWkdXbE5TYlZaR1RWVldVbGRIYUU5V2ExWkhUVEZTVjFW" \
               "cldteFNWRVpHVlZab2IxUnNXa1pXYWxKVlZteEtSMVZHUlRsUVVUMDk="

output_string = ""

for i in range(5):
    input_string = base64.b64decode(input_string)

output_string = bin_decode(input_string)
print(output_string)
