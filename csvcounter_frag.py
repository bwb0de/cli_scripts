				
			#if check_item_list(mk_tmp_cross_key, cross_key_list) == False:
				#cross_key = mk_tmp_cross_key
				#tmp_csv_line[cross_key] = {}
				#colanalisis = []
				#for lines in csv_content:
					#line_cross_value = ' e '.join([lines[c],lines[cc],lines[ccc],lines[cccc],lines[ccccc]])
					#colanalisis.append(line_cross_value)
				#cros_col_total = 0
				#for unic_line in set(colanalisis):
					#tmp_csv_line[cross_key][unic_line] = [colanalisis.count(unic_line)]
					#cros_col_total += colanalisis.count(unic_line)
				#tmp_csv_line_fa_total[cross_key] = cros_col_total
			
			
		#for c in sorted(csv_cols):
			#for cc in sorted(csv_cols):
				#for ccc in sorted(csv_cols):
					#for cccc in sorted(csv_cols):
						#for ccccc in sorted(csv_cols):
							#if (c != cc) and (c != ccc) and (c != cccc) and (c != ccccc) and (cc != ccc) and (cc != cccc) and (cc != ccccc) and (ccc != cccc) and (ccc != ccccc) and (cccc != ccccc):
									#mk_tmp_cross_key = [c,cc,ccc,cccc,ccccc]
									#mk_tmp_cross_key.sort()
									#mk_tmp_cross_key = ' e '.join(mk_tmp_cross_key)
									#if check_item_list(mk_tmp_cross_key, cross_key_list) == False:
										#cross_key = mk_tmp_cross_key
										#tmp_csv_line[cross_key] = {}
										#colanalisis = []
										#for lines in csv_content:
											#line_cross_value = ' e '.join([lines[c],lines[cc],lines[ccc],lines[cccc],lines[ccccc]])
											#colanalisis.append(line_cross_value)
										#cros_col_total = 0
										#for unic_line in set(colanalisis):
											#tmp_csv_line[cross_key][unic_line] = [colanalisis.count(unic_line)]
											#cros_col_total += colanalisis.count(unic_line)
										#tmp_csv_line_fa_total[cross_key] = cros_col_total
