"""Simplified operating result, not cash flow or investment appraisal."""
import math
def result(price,variable,volume,fixed):
 for x in (price,variable,volume,fixed):
  if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x) or x<0:raise ValueError('finite nonnegative inputs required')
 margin=price-variable
 return {'contribution':margin,'operating_result':margin*volume-fixed,'break_even_volume':fixed/margin if margin>0 else None}
