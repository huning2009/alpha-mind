SELECT array_to_string(ARRAY(SELECT 'u' || '.' || '"' || c.column_name || '"'
        FROM information_schema.columns As c
            WHERE table_name = 'uqer'
            AND  c.column_name NOT IN('trade_date', 'code')
    ), ',') || ' FROM uqer AS u' As sqlstmt2;


SELECT array_to_string(ARRAY(SELECT 'l' || '.' || '"' || c.column_name || '"'
        FROM information_schema.columns As c
            WHERE table_name = 'legacy_factor'
            AND  c.column_name NOT IN('trade_date', 'code')
    ), ',') || ' FROM legacy_factor AS l' As sqlstmt3;


SELECT array_to_string(ARRAY(SELECT 't' || '.' || '"' || c.column_name || '"'
        FROM information_schema.columns As c
            WHERE table_name = 'tiny'
            AND  c.column_name NOT IN('trade_date', 'code')
    ), ',') || ' FROM tiny AS t' As sqlstmt4;


SELECT array_to_string(ARRAY(SELECT 'r' || '.' || '"' || c.column_name || '"'
        FROM information_schema.columns As c
            WHERE table_name = 'risk_exposure'
            AND  c.column_name NOT IN('trade_date', 'code')
    ), ',') || ' FROM risk_exposure AS r' As sqlstmt5;


create MATERIALIZED VIEW full_factor_view as SELECT m."trade_date",m."code",m."secShortName",m."exchangeCD",m."preClosePrice",m."actPreClosePrice",m."openPrice",m."highestPrice",m."lowestPrice",m."closePrice",m."turnoverVol",m."turnoverValue",m."dealAmount",m."turnoverRate",m."accumAdjFactor",m."negMarketValue",m."marketValue",m."chgPct",m."isOpen",m."vwap",
u."AccountsPayablesTDays",u."AccountsPayablesTRate",u."AdminiExpenseRate",u."ARTDays",u."ARTRate",u."ASSI",u."BLEV",u."BondsPayableToAsset",u."CashRateOfSales",u."CashToCurrentLiability",u."CMRA",u."CTOP",u."CTP5",u."CurrentAssetsRatio",u."CurrentAssetsTRate",u."CurrentRatio",u."DAVOL10",u."DAVOL20",u."DAVOL5",u."DDNBT",u."DDNCR",u."DDNSR",u."DebtEquityRatio",u."DebtsAssetRatio",u."DHILO",u."DilutedEPS",u."DVRAT",u."EBITToTOR",u."EGRO",u."EMA10",u."EMA120",u."EMA20",u."EMA5",u."EMA60",u."EPS",u."EquityFixedAssetRatio",u."EquityToAsset",u."EquityTRate",u."ETOP",u."ETP5",u."FinancialExpenseRate",u."FinancingCashGrowRate",u."FixAssetRatio",u."FixedAssetsTRate",u."GrossIncomeRatio",u."HBETA",u."HSIGMA",u."IntangibleAssetRatio",u."InventoryTDays",u."InventoryTRate",u."InvestCashGrowRate",u."LCAP",u."LFLO",u."LongDebtToAsset",u."LongDebtToWorkingCapital",u."LongTermDebtToAsset",u."MA10",u."MA120",u."MA20",u."MA5",u."MA60",u."MAWVAD",u."MFI",u."MLEV",u."NetAssetGrowRate",u."NetProfitGrowRate",u."NetProfitRatio",u."NOCFToOperatingNI",u."NonCurrentAssetsRatio",u."NPParentCompanyGrowRate",u."NPToTOR",u."OperatingExpenseRate",u."OperatingProfitGrowRate",u."OperatingProfitRatio",u."OperatingProfitToTOR",u."OperatingRevenueGrowRate",u."OperCashGrowRate",u."OperCashInToCurrentLiability",u."PB",u."PCF",u."PE",u."PS",u."PSY",u."QuickRatio",u."REVS10",u."REVS20",u."REVS5",u."ROA",u."ROA5",u."ROE",u."ROE5",u."RSI",u."RSTR12",u."RSTR24",u."SalesCostRatio",u."SaleServiceCashToOR",u."SUE",u."TaxRatio",u."TOBT",u."TotalAssetGrowRate",u."TotalAssetsTRate",u."TotalProfitCostRatio",u."TotalProfitGrowRate",u."VOL10",u."VOL120",u."VOL20",u."VOL240",u."VOL5",u."VOL60",u."WVAD",u."REC",u."DAREC",u."GREC",u."FY12P",u."DAREV",u."GREV",u."SFY12P",u."DASREV",u."GSREV",u."FEARNG",u."FSALESG",u."TA2EV",u."CFO2EV",u."ACCA",u."DEGM",u."SUOI",u."EARNMOM",u."FiftyTwoWeekHigh",u."Volatility",u."Skewness",u."ILLIQUIDITY",u."BackwardADJ",u."MACD",u."ADTM",u."ATR14",u."ATR6",u."BIAS10",u."BIAS20",u."BIAS5",u."BIAS60",u."BollDown",u."BollUp",u."CCI10",u."CCI20",u."CCI5",u."CCI88",u."KDJ_K",u."KDJ_D",u."KDJ_J",u."ROC6",u."ROC20",u."SBM",u."STM",u."UpRVI",u."DownRVI",u."RVI",u."SRMI",u."ChandeSD",u."ChandeSU",u."CMO",u."DBCD",u."ARC",u."OBV",u."OBV6",u."OBV20",u."TVMA20",u."TVMA6",u."TVSTD20",u."TVSTD6",u."VDEA",u."VDIFF",u."VEMA10",u."VEMA12",u."VEMA26",u."VEMA5",u."VMACD",u."VOSC",u."VR",u."VROC12",u."VROC6",u."VSTD10",u."VSTD20",u."KlingerOscillator",u."MoneyFlow20",u."AD",u."AD20",u."AD6",u."CoppockCurve",u."ASI",u."ChaikinOscillator",u."ChaikinVolatility",u."EMV14",u."EMV6",u."plusDI",u."minusDI",u."ADX",u."ADXR",u."Aroon",u."AroonDown",u."AroonUp",u."DEA",u."DIFF",u."DDI",u."DIZ",u."DIF",u."MTM",u."MTMMA",u."PVT",u."PVT6",u."PVT12",u."TRIX5",u."TRIX10",u."UOS",u."MA10RegressCoeff12",u."MA10RegressCoeff6",u."PLRC6",u."PLRC12",u."SwingIndex",u."Ulcer10",u."Ulcer5",u."Hurst",u."ACD6",u."ACD20",u."EMA12",u."EMA26",u."APBMA",u."BBI",u."BBIC",u."TEMA10",u."TEMA5",u."MA10Close",u."AR",u."BR",u."ARBR",u."CR20",u."MassIndex",u."BearPower",u."BullPower",u."Elder",u."NVI",u."PVI",u."RC12",u."RC24",u."JDQS20",u."Variance20",u."Variance60",u."Variance120",u."Kurtosis20",u."Kurtosis60",u."Kurtosis120",u."Alpha20",u."Alpha60",u."Alpha120",u."Beta20",u."Beta60",u."Beta120",u."SharpeRatio20",u."SharpeRatio60",u."SharpeRatio120",u."TreynorRatio20",u."TreynorRatio60",u."TreynorRatio120",u."InformationRatio20",u."InformationRatio60",u."InformationRatio120",u."GainVariance20",u."GainVariance60",u."GainVariance120",u."LossVariance20",u."LossVariance60",u."LossVariance120",u."GainLossVarianceRatio20",u."GainLossVarianceRatio60",u."GainLossVarianceRatio120",u."RealizedVolatility",u."REVS60",u."REVS120",u."REVS250",u."REVS750",u."REVS5m20",u."REVS5m60",u."REVS5Indu1",u."REVS20Indu1",u."Volumn1M",u."Volumn3M",u."Price1M",u."Price3M",u."Price1Y",u."Rank1M",u."CashDividendCover",u."DividendCover",u."DividendPaidRatio",u."RetainedEarningRatio",u."CashEquivalentPS",u."DividendPS",u."EPSTTM",u."NetAssetPS",u."TORPS",u."TORPSLatest",u."OperatingRevenuePS",u."OperatingRevenuePSLatest",u."OperatingProfitPS",u."OperatingProfitPSLatest",u."CapitalSurplusFundPS",u."SurplusReserveFundPS",u."UndividedProfitPS",u."RetainedEarningsPS",u."OperCashFlowPS",u."CashFlowPS",u."NetNonOIToTP",u."NetNonOIToTPLatest",u."PeriodCostsRate",u."InterestCover",u."NetProfitGrowRate3Y",u."NetProfitGrowRate5Y",u."OperatingRevenueGrowRate3Y",u."OperatingRevenueGrowRate5Y",u."NetCashFlowGrowRate",u."NetProfitCashCover",u."OperCashInToAsset",u."CashConversionCycle",u."OperatingCycle",u."PEG3Y",u."PEG5Y",u."PEIndu",u."PBIndu",u."PSIndu",u."PCFIndu",u."PEHist20",u."PEHist60",u."PEHist120",u."PEHist250",u."StaticPE",u."ForwardPE",u."EnterpriseFCFPS",u."ShareholderFCFPS",u."ROEDiluted",u."ROEAvg",u."ROEWeighted",u."ROECut",u."ROECutWeighted",u."ROIC",u."ROAEBIT",u."ROAEBITTTM",u."OperatingNIToTP",u."OperatingNIToTPLatest",u."InvestRAssociatesToTP",u."InvestRAssociatesToTPLatest",u."NPCutToNP",u."SuperQuickRatio",u."TSEPToInterestBearDebt",u."DebtTangibleEquityRatio",u."TangibleAToInteBearDebt",u."TangibleAToNetDebt",u."NOCFToTLiability",u."NOCFToInterestBearDebt",u."NOCFToNetDebt",u."TSEPToTotalCapital",u."InteBearDebtToTotalCapital",u."NPParentCompanyCutYOY",u."SalesServiceCashToORLatest",u."CashRateOfSalesLatest",u."NOCFToOperatingNILatest",u."TotalAssets",u."MktValue",u."NegMktValue",u."TEAP",u."NIAP",u."TotalFixedAssets",u."IntFreeCL",u."IntFreeNCL",u."IntCL",u."IntDebt",u."NetDebt",u."NetTangibleAssets",u."WorkingCapital",u."NetWorkingCapital",u."TotalPaidinCapital",u."RetainedEarnings",u."OperateNetIncome",u."ValueChgProfit",u."NetIntExpense",u."EBIT",u."EBITDA",u."EBIAT",u."NRProfitLoss",u."NIAPCut",u."FCFF",u."FCFE",u."DA",u."TRevenueTTM",u."TCostTTM",u."RevenueTTM",u."CostTTM",u."GrossProfitTTM",u."SalesExpenseTTM",u."AdminExpenseTTM",u."FinanExpenseTTM",u."AssetImpairLossTTM",u."NPFromOperatingTTM",u."NPFromValueChgTTM",u."OperateProfitTTM",u."NonOperatingNPTTM",u."TProfitTTM",u."NetProfitTTM",u."NetProfitAPTTM",u."SaleServiceRenderCashTTM",u."NetOperateCFTTM",u."NetInvestCFTTM",u."NetFinanceCFTTM",u."GrossProfit",u."Beta252",u."RSTR504",u."EPIBS",u."CETOP",u."DASTD",u."CmraCNE5",u."HsigmaCNE5",u."SGRO",u."EgibsLong",u."STOM",u."STOQ",u."STOA",u."NLSIZE",
 l."ROEAfterNonRecurring",l."EPSAfterNonRecurring",l."EODPrice",l."LogFloatCap",l."BPS",l."SPS",l."DebtToAsset",l."DROEAfterNonRecurring",l."LogTotalCap",l."BP",l."SP",l."EPAfterNonRecurring",l."DivToB",l."DivP",l."EBITToSales",l."EBITAToSales",l."EVToSales",l."EVToEBIT",l."EVToEBITDA",l."EVToNOPLAT",l."EVToIC",l."FCFFPS",l."FCFFToEarningAfterNonRecurring",l."FCFFP",l."ProfitToAsset",l."GrossProfitRatio",l."LATO",l."FATO",l."TATO",l."EquityTO",l."PayableTO",l."RecievableTO",l."RevenueGrowth",l."GrossProfitGrowth",l."NetProfitGrowth",l."GrossCFToRevenue",l."CFToRevenue",l."CFToProfit",l."CFToAsset",l."GrossCFGrowth",l."CFGrowth",l."ICFGrowth",l."AveAmount60",l."PeriodReturn60",l."AmountRatio60to250",l."CFPS",l."CFP",l."NetCFGrowth",l."NetCFGrowthP",l."NetCash",l."NetCashP",l."BVPSGrowth",l."EquityPSGrowth",l."WholeSales",l."WholeProfitAfterNonRecurring",l."ExpenseRatio",l."AcidTestRatio",l."TimeInterestEarnedRatio",l."DepositReceivedVsSale",l."DebtRatioExcemptDepRec",l."SNBARatio",
  t."CFinc1",t."BDTO",t."RVOL",t."CHV",t."VAL",
  r."BETA",r."MOMENTUM",r."SIZE",r."EARNYILD",r."RESVOL",r."GROWTH",r."BTOP",r."LEVERAGE",r."LIQUIDTY",r."SIZENL",r."Bank",r."RealEstate",r."Health",r."Transportation",r."Mining",r."NonFerMetal",r."HouseApp",r."LeiService",r."MachiEquip",r."BuildDeco",r."CommeTrade",r."CONMAT",r."Auto",r."Textile",r."FoodBever",r."Electronics",r."Computer",r."LightIndus",r."Utilities",r."Telecom",r."AgriForest",r."CHEM",r."Media",r."IronSteel",r."NonBankFinan",r."ELECEQP",r."AERODEF",r."Conglomerates",r."COUNTRY",
  e."DROE",e."IVR",e."xueqiu_hotness",
  s1."SRISK" as d_srisk, s2."SRISK" as s_srisk, s3."SRISK" as l_srisk
 FROM market AS m left join uqer AS u on m.trade_date = u.trade_date and m.code = u.code
 inner join risk_exposure AS r on m.trade_date = r.trade_date and m.code = r.code
 inner join specific_risk_day as s1 on m.trade_date = s1.trade_date and m.code = s1.code
 inner join specific_risk_short as s2 on m.trade_date = s2.trade_date and m.code = s2.code
 inner join specific_risk_long as s3 on m.trade_date = s3.trade_date and m.code = s3.code
 left join legacy_factor as l on m.trade_date = l.trade_date and m.code = l.code
 left join tiny as t on m.trade_date = t.trade_date and m.code = t.code
 left join experimental as e on m.trade_date = e.trade_date and m.code = e.code;

create UNIQUE index on full_factor_view (trade_date, code);