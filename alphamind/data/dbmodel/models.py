# -*- coding: utf-8 -*-
"""
Created on 2017-6-29

@author: cheng.li
"""

from sqlalchemy import BigInteger, Column, DateTime, Float, Index, Integer, String, Table, Text, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class DailyReturn(Base):
    __tablename__ = 'daily_return'
    __table_args__ = (
        Index('daily_return_Date_Code_uindex', 'Date', 'Code', unique=True),
    )

    Date = Column(DateTime, primary_key=True, nullable=False)
    Code = Column(Integer, primary_key=True, nullable=False)
    d1 = Column(Float(53))


class FactorMaster(Base):
    __tablename__ = 'factor_master'
    __table_args__ = (
        Index('factor_master_factor_source_uindex', 'factor', 'source', unique=True),
    )

    factor = Column(String(30, 'utf8_general_ci'), primary_key=True, nullable=False)
    source = Column(String(30, 'utf8_general_ci'), primary_key=True, nullable=False)
    alias = Column(String(50, 'utf8_general_ci'), nullable=False)
    updateTime = Column(DateTime)
    description = Column(Text(2147483647, 'utf8_general_ci'))


class HaltList(Base):
    __tablename__ = 'halt_list'
    __table_args__ = (
        Index('halt_list_Date_Code_haltBeginTime_uindex', 'Date', 'Code', 'haltBeginTime', unique=True),
    )

    Date = Column(DateTime, primary_key=True, nullable=False)
    Code = Column(Integer, primary_key=True, nullable=False)
    haltBeginTime = Column(DateTime, primary_key=True, nullable=False)
    haltEndTime = Column(DateTime)
    secShortName = Column(String(20, 'utf8_general_ci'))
    exchangeCD = Column(String(4, 'utf8_general_ci'))
    listStatusCD = Column(String(4, 'utf8_general_ci'))
    delistDate = Column(DateTime)
    assetClass = Column(String(4, 'utf8_general_ci'))


class IndexComponent(Base):
    __tablename__ = 'index_components'
    __table_args__ = (
        Index('index_components_Date_indexCode_Code_uindex', 'Date', 'indexCode', 'Code', unique=True),
    )

    Date = Column(DateTime, primary_key=True, nullable=False)
    Code = Column(Integer, primary_key=True, nullable=False)
    effDate = Column(DateTime)
    indexShortName = Column(String(20, 'utf8_general_ci'))
    indexCode = Column(Integer, primary_key=True, nullable=False)
    secShortName = Column(String(20, 'utf8_general_ci'))
    exchangeCD = Column(String(4, 'utf8_general_ci'))
    weight = Column(Float(53))


class Industry(Base):
    __tablename__ = 'industry'
    __table_args__ = (
        Index('industry_Date_Code_industryID_uindex', 'Date', 'Code', 'industryID', unique=True),
    )

    Date = Column(DateTime, primary_key=True, nullable=False)
    Code = Column(Integer, primary_key=True, nullable=False)
    industry = Column(String(30, 'utf8_general_ci'), nullable=False)
    industryID = Column(BigInteger, primary_key=True, nullable=False)
    industrySymbol = Column(String(20, 'utf8_general_ci'))
    industryID1 = Column(BigInteger, nullable=False)
    industryName1 = Column(String(50, 'utf8_general_ci'))
    industryID2 = Column(BigInteger)
    industryName2 = Column(String(50, 'utf8_general_ci'))
    industryID3 = Column(BigInteger)
    industryName3 = Column(String(50, 'utf8_general_ci'))
    IndustryID4 = Column(BigInteger)
    IndustryName4 = Column(String(50, 'utf8_general_ci'))


class LegacyFactor(Base):
    __tablename__ = 'legacy_factor'
    __table_args__ = (
        Index('legacy_factor_Date_Code_uindex', 'Date', 'Code', unique=True),
    )

    Date = Column(DateTime, primary_key=True, nullable=False)
    Code = Column(Integer, primary_key=True, nullable=False)
    ROEAfterNonRecurring = Column(Float(53))
    EPSAfterNonRecurring = Column(Float(53))
    EODPrice = Column(Float(53))
    LogFloatCap = Column(Float(53))
    BPS = Column(Float(53))
    SPS = Column(Float(53))
    DebtToAsset = Column(Float(53))
    STOM = Column(Float(53))
    DROEAfterNonRecurring = Column(Float(53))
    LogTotalCap = Column(Float(53))
    BP = Column(Float(53))
    SP = Column(Float(53))
    EPAfterNonRecurring = Column(Float(53))
    DivToB = Column(Float(53))
    DivP = Column(Float(53))
    EBITToSales = Column(Float(53))
    EBITAToSales = Column(Float(53))
    EVToSales = Column(Float(53))
    EVToEBIT = Column(Float(53))
    EVToEBITDA = Column(Float(53))
    EVToNOPLAT = Column(Float(53))
    EVToIC = Column(Float(53))
    ROIC = Column(Float(53))
    FCFFPS = Column(Float(53))
    FCFFToEarningAfterNonRecurring = Column(Float(53))
    FCFFP = Column(Float(53))
    ProfitToAsset = Column(Float(53))
    GrossProfitRatio = Column(Float(53))
    NetProfitRatio = Column(Float(53))
    LATO = Column(Float(53))
    FATO = Column(Float(53))
    TATO = Column(Float(53))
    EquityTO = Column(Float(53))
    PayableTO = Column(Float(53))
    RecievableTO = Column(Float(53))
    RevenueGrowth = Column(Float(53))
    GrossProfitGrowth = Column(Float(53))
    NetProfitGrowth = Column(Float(53))
    GrossCFToRevenue = Column(Float(53))
    CFToRevenue = Column(Float(53))
    CFToProfit = Column(Float(53))
    CFToAsset = Column(Float(53))
    GrossCFGrowth = Column(Float(53))
    CFGrowth = Column(Float(53))
    ICFGrowth = Column(Float(53))
    AveAmount60 = Column(Float(53))
    PeriodReturn60 = Column(Float(53))
    AmountRatio60to250 = Column(Float(53))
    CFPS = Column(Float(53))
    CFP = Column(Float(53))
    NetCFGrowth = Column(Float(53))
    NetCFGrowthP = Column(Float(53))
    NetCash = Column(Float(53))
    NetCashP = Column(Float(53))
    BVPSGrowth = Column(Float(53))
    EquityPSGrowth = Column(Float(53))
    WholeSales = Column(Float(53))
    WholeProfitAfterNonRecurring = Column(Float(53))
    ExpenseRatio = Column(Float(53))
    CurrentRatio = Column(Float(53))
    QuickRatio = Column(Float(53))
    AcidTestRatio = Column(Float(53))
    TimeInterestEarnedRatio = Column(Float(53))
    DepositReceivedVsSale = Column(Float(53))
    DebtRatioExcemptDepRec = Column(Float(53))
    SNBARatio = Column(Float(53))


class Market(Base):
    __tablename__ = 'market'
    __table_args__ = (
        Index('market_Date_Code_uindex', 'Date', 'Code', unique=True),
    )

    Date = Column(DateTime, primary_key=True, nullable=False)
    Code = Column(Integer, primary_key=True, nullable=False)
    secShortName = Column(String(10, 'utf8_general_ci'))
    exchangeCD = Column(String(4, 'utf8_general_ci'))
    preClosePrice = Column(Float(53))
    actPreClosePrice = Column(Float(53))
    openPrice = Column(Float(53))
    highestPrice = Column(Float(53))
    lowestPrice = Column(Float(53))
    closePrice = Column(Float(53))
    turnoverVol = Column(BigInteger)
    turnoverValue = Column(Float(53))
    dealAmount = Column(BigInteger)
    turnoverRate = Column(Float(53))
    accumAdjFactor = Column(Float(53))
    negMarketValue = Column(Float(53))
    marketValue = Column(Float(53))
    chgPct = Column(Float(53))
    PE = Column(Float(53))
    PE1 = Column(Float(53))
    PB = Column(Float(53))
    isOpen = Column(Integer)


class Performance(Base):
    __tablename__ = 'performance'
    __table_args__ = (
        Index('performance_Date_type_portfolio_industry_source_universe_uindex', 'Date', 'type', 'portfolio', 'industry', 'source', 'universe', unique=True),
        Index('performance_type_industry_universe_portfolio_index', 'type', 'industry', 'universe', 'portfolio')
    )

    Date = Column(DateTime, primary_key=True, nullable=False)
    type = Column(String(20, 'utf8_general_ci'), primary_key=True, nullable=False)
    portfolio = Column(String(50, 'utf8_general_ci'), primary_key=True, nullable=False)
    industry = Column(String(50, 'utf8_general_ci'), primary_key=True, nullable=False)
    source = Column(String(20, 'utf8_general_ci'), primary_key=True, nullable=False)
    universe = Column(String(50, 'utf8_general_ci'), primary_key=True, nullable=False)
    er = Column(Float(53), nullable=False)
    turn_over = Column(Float(53))
    ic = Column(Float(53))


class Performance2(Base):
    __tablename__ = 'performance2'
    __table_args__ = (
        Index('performance2_Date_type_portfolio_industry_source_universe_uindex', 'Date', 'type', 'portfolio', 'industry', 'source', 'universe', 'benchmark', unique=True),
        Index('performance2_type_industry_universe_portfolio_index', 'type', 'industry', 'universe', 'portfolio')
    )

    Date = Column(DateTime, primary_key=True, nullable=False)
    type = Column(String(20, 'utf8_general_ci'), primary_key=True, nullable=False)
    portfolio = Column(String(50, 'utf8_general_ci'), primary_key=True, nullable=False)
    industry = Column(String(50, 'utf8_general_ci'), primary_key=True, nullable=False)
    source = Column(String(20, 'utf8_general_ci'), primary_key=True, nullable=False)
    universe = Column(String(50, 'utf8_general_ci'), primary_key=True, nullable=False)
    benchmark = Column(Integer, primary_key=True, nullable=False)
    er = Column(Float(53), nullable=False)
    turn_over = Column(Float(53))
    ic = Column(Float(53))


class RiskCovDay(Base):
    __tablename__ = 'risk_cov_day'
    __table_args__ = (
        Index('risk_cov_day_Date_Factor_uindex', 'Date', 'Factor', unique=True),
        Index('risk_cov_day_Date_FactorID_uindex', 'Date', 'FactorID', unique=True)
    )

    Date = Column(DateTime, primary_key=True, nullable=False)
    FactorID = Column(Integer)
    Factor = Column(String(50, 'utf8_general_ci'), primary_key=True, nullable=False)
    BETA = Column(Float(53))
    MOMENTUM = Column(Float(53))
    SIZE = Column(Float(53))
    EARNYILD = Column(Float(53))
    RESVOL = Column(Float(53))
    GROWTH = Column(Float(53))
    BTOP = Column(Float(53))
    LEVERAGE = Column(Float(53))
    LIQUIDTY = Column(Float(53))
    SIZENL = Column(Float(53))
    Bank = Column(Float(53))
    RealEstate = Column(Float(53))
    Health = Column(Float(53))
    Transportation = Column(Float(53))
    Mining = Column(Float(53))
    NonFerMetal = Column(Float(53))
    HouseApp = Column(Float(53))
    LeiService = Column(Float(53))
    MachiEquip = Column(Float(53))
    BuildDeco = Column(Float(53))
    CommeTrade = Column(Float(53))
    CONMAT = Column(Float(53))
    Auto = Column(Float(53))
    Textile = Column(Float(53))
    FoodBever = Column(Float(53))
    Electronics = Column(Float(53))
    Computer = Column(Float(53))
    LightIndus = Column(Float(53))
    Utilities = Column(Float(53))
    Telecom = Column(Float(53))
    AgriForest = Column(Float(53))
    CHEM = Column(Float(53))
    Media = Column(Float(53))
    IronSteel = Column(Float(53))
    NonBankFinan = Column(Float(53))
    ELECEQP = Column(Float(53))
    AERODEF = Column(Float(53))
    Conglomerates = Column(Float(53))
    COUNTRY = Column(Float(53))
    updateTime = Column(DateTime)


class RiskCovLong(Base):
    __tablename__ = 'risk_cov_long'
    __table_args__ = (
        Index('risk_cov_long_Date_FactorID_uindex', 'Date', 'FactorID', unique=True),
        Index('risk_cov_long_Date_Factor_uindex', 'Date', 'Factor', unique=True)
    )

    Date = Column(DateTime, primary_key=True, nullable=False)
    FactorID = Column(Integer)
    Factor = Column(String(50, 'utf8_general_ci'), primary_key=True, nullable=False)
    BETA = Column(Float(53))
    MOMENTUM = Column(Float(53))
    SIZE = Column(Float(53))
    EARNYILD = Column(Float(53))
    RESVOL = Column(Float(53))
    GROWTH = Column(Float(53))
    BTOP = Column(Float(53))
    LEVERAGE = Column(Float(53))
    LIQUIDTY = Column(Float(53))
    SIZENL = Column(Float(53))
    Bank = Column(Float(53))
    RealEstate = Column(Float(53))
    Health = Column(Float(53))
    Transportation = Column(Float(53))
    Mining = Column(Float(53))
    NonFerMetal = Column(Float(53))
    HouseApp = Column(Float(53))
    LeiService = Column(Float(53))
    MachiEquip = Column(Float(53))
    BuildDeco = Column(Float(53))
    CommeTrade = Column(Float(53))
    CONMAT = Column(Float(53))
    Auto = Column(Float(53))
    Textile = Column(Float(53))
    FoodBever = Column(Float(53))
    Electronics = Column(Float(53))
    Computer = Column(Float(53))
    LightIndus = Column(Float(53))
    Utilities = Column(Float(53))
    Telecom = Column(Float(53))
    AgriForest = Column(Float(53))
    CHEM = Column(Float(53))
    Media = Column(Float(53))
    IronSteel = Column(Float(53))
    NonBankFinan = Column(Float(53))
    ELECEQP = Column(Float(53))
    AERODEF = Column(Float(53))
    Conglomerates = Column(Float(53))
    COUNTRY = Column(Float(53))
    updateTime = Column(DateTime)


class RiskCovShort(Base):
    __tablename__ = 'risk_cov_short'
    __table_args__ = (
        Index('risk_cov_short_Date_Factor_uindex', 'Date', 'Factor', unique=True),
        Index('risk_cov_short_Date_FactorID_uindex', 'Date', 'FactorID', unique=True)
    )

    Date = Column(DateTime, primary_key=True, nullable=False)
    FactorID = Column(Integer)
    Factor = Column(String(50, 'utf8_general_ci'), primary_key=True, nullable=False)
    BETA = Column(Float(53))
    MOMENTUM = Column(Float(53))
    SIZE = Column(Float(53))
    EARNYILD = Column(Float(53))
    RESVOL = Column(Float(53))
    GROWTH = Column(Float(53))
    BTOP = Column(Float(53))
    LEVERAGE = Column(Float(53))
    LIQUIDTY = Column(Float(53))
    SIZENL = Column(Float(53))
    Bank = Column(Float(53))
    RealEstate = Column(Float(53))
    Health = Column(Float(53))
    Transportation = Column(Float(53))
    Mining = Column(Float(53))
    NonFerMetal = Column(Float(53))
    HouseApp = Column(Float(53))
    LeiService = Column(Float(53))
    MachiEquip = Column(Float(53))
    BuildDeco = Column(Float(53))
    CommeTrade = Column(Float(53))
    CONMAT = Column(Float(53))
    Auto = Column(Float(53))
    Textile = Column(Float(53))
    FoodBever = Column(Float(53))
    Electronics = Column(Float(53))
    Computer = Column(Float(53))
    LightIndus = Column(Float(53))
    Utilities = Column(Float(53))
    Telecom = Column(Float(53))
    AgriForest = Column(Float(53))
    CHEM = Column(Float(53))
    Media = Column(Float(53))
    IronSteel = Column(Float(53))
    NonBankFinan = Column(Float(53))
    ELECEQP = Column(Float(53))
    AERODEF = Column(Float(53))
    Conglomerates = Column(Float(53))
    COUNTRY = Column(Float(53))
    updateTime = Column(DateTime)


class RiskExposure(Base):
    __tablename__ = 'risk_exposure'
    __table_args__ = (
        Index('risk_exposure_Date_Code_uindex', 'Date', 'Code', unique=True),
    )

    Date = Column(DateTime, primary_key=True, nullable=False)
    Code = Column(Integer, primary_key=True, nullable=False)
    exchangeCD = Column(String(4, 'utf8_general_ci'))
    secShortName = Column(String(20, 'utf8_general_ci'))
    BETA = Column(Float(53))
    MOMENTUM = Column(Float(53))
    SIZE = Column(Float(53))
    EARNYILD = Column(Float(53))
    RESVOL = Column(Float(53))
    GROWTH = Column(Float(53))
    BTOP = Column(Float(53))
    LEVERAGE = Column(Float(53))
    LIQUIDTY = Column(Float(53))
    SIZENL = Column(Float(53))
    Bank = Column(BigInteger)
    RealEstate = Column(BigInteger)
    Health = Column(BigInteger)
    Transportation = Column(BigInteger)
    Mining = Column(BigInteger)
    NonFerMetal = Column(BigInteger)
    HouseApp = Column(BigInteger)
    LeiService = Column(BigInteger)
    MachiEquip = Column(BigInteger)
    BuildDeco = Column(BigInteger)
    CommeTrade = Column(BigInteger)
    CONMAT = Column(BigInteger)
    Auto = Column(BigInteger)
    Textile = Column(BigInteger)
    FoodBever = Column(BigInteger)
    Electronics = Column(BigInteger)
    Computer = Column(BigInteger)
    LightIndus = Column(BigInteger)
    Utilities = Column(BigInteger)
    Telecom = Column(BigInteger)
    AgriForest = Column(BigInteger)
    CHEM = Column(BigInteger)
    Media = Column(BigInteger)
    IronSteel = Column(BigInteger)
    NonBankFinan = Column(BigInteger)
    ELECEQP = Column(BigInteger)
    AERODEF = Column(BigInteger)
    Conglomerates = Column(BigInteger)
    COUNTRY = Column(BigInteger)
    updateTime = Column(DateTime)


t_risk_master = Table(
    'risk_master', metadata,
    Column('factor', String(30, 'utf8_general_ci'), nullable=False),
    Column('source', String(30, 'utf8_general_ci'), nullable=False),
    Column('alias', String(30, 'utf8_general_ci'), nullable=False),
    Column('type', String(30, 'utf8_general_ci')),
    Column('updateTime', DateTime),
    Column('description', Text(2147483647, 'utf8_general_ci')),
    Column('factor_id', Integer, nullable=False)
)


class RiskReturn(Base):
    __tablename__ = 'risk_return'

    Date = Column(DateTime, primary_key=True, unique=True)
    BETA = Column(Float(53))
    MOMENTUM = Column(Float(53))
    SIZE = Column(Float(53))
    EARNYILD = Column(Float(53))
    RESVOL = Column(Float(53))
    GROWTH = Column(Float(53))
    BTOP = Column(Float(53))
    LEVERAGE = Column(Float(53))
    LIQUIDTY = Column(Float(53))
    SIZENL = Column(Float(53))
    Bank = Column(Float(53))
    RealEstate = Column(Float(53))
    Health = Column(Float(53))
    Transportation = Column(Float(53))
    Mining = Column(Float(53))
    NonFerMetal = Column(Float(53))
    HouseApp = Column(Float(53))
    LeiService = Column(Float(53))
    MachiEquip = Column(Float(53))
    BuildDeco = Column(Float(53))
    CommeTrade = Column(Float(53))
    CONMAT = Column(Float(53))
    Auto = Column(Float(53))
    Textile = Column(Float(53))
    FoodBever = Column(Float(53))
    Electronics = Column(Float(53))
    Computer = Column(Float(53))
    LightIndus = Column(Float(53))
    Utilities = Column(Float(53))
    Telecom = Column(Float(53))
    AgriForest = Column(Float(53))
    CHEM = Column(Float(53))
    Media = Column(Float(53))
    IronSteel = Column(Float(53))
    NonBankFinan = Column(Float(53))
    ELECEQP = Column(Float(53))
    AERODEF = Column(Float(53))
    Conglomerates = Column(Float(53))
    COUNTRY = Column(Float(53))
    updateTime = Column(DateTime)


class SpecificReturn(Base):
    __tablename__ = 'specific_return'
    __table_args__ = (
        Index('specific_return_Date_Code_uindex', 'Date', 'Code', unique=True),
    )

    Date = Column(DateTime, primary_key=True, nullable=False)
    Code = Column(Integer, primary_key=True, nullable=False)
    exchangeCD = Column(String(4, 'utf8_general_ci'))
    secShortName = Column(String(20, 'utf8_general_ci'))
    spret = Column(Float(53))
    updateTime = Column(DateTime)


class SpecificRiskDay(Base):
    __tablename__ = 'specific_risk_day'
    __table_args__ = (
        Index('specific_risk_day_Date_Code_uindex', 'Date', 'Code', unique=True),
    )

    Date = Column(DateTime, primary_key=True, nullable=False)
    Code = Column(Integer, primary_key=True, nullable=False)
    exchangeCD = Column(String(4, 'utf8_general_ci'))
    secShortName = Column(String(20, 'utf8_general_ci'))
    SRISK = Column(Float(53))
    updateTime = Column(DateTime)


class SpecificRiskLong(Base):
    __tablename__ = 'specific_risk_long'
    __table_args__ = (
        Index('specific_risk_long_Date_Code_uindex', 'Date', 'Code', unique=True),
    )

    Date = Column(DateTime, primary_key=True, nullable=False)
    Code = Column(Integer, primary_key=True, nullable=False)
    exchangeCD = Column(String(4, 'utf8_general_ci'))
    secShortName = Column(String(20, 'utf8_general_ci'))
    updateTime = Column(DateTime)
    SRISK = Column(Float(53))


class SpecificRiskShort(Base):
    __tablename__ = 'specific_risk_short'
    __table_args__ = (
        Index('specific_risk_short_Date_Code_uindex', 'Date', 'Code', unique=True),
    )

    Date = Column(DateTime, primary_key=True, nullable=False)
    Code = Column(Integer, primary_key=True, nullable=False)
    exchangeCD = Column(String(4, 'utf8_general_ci'))
    secShortName = Column(String(20, 'utf8_general_ci'))
    SRISK = Column(Float(53))
    updateTime = Column(DateTime)


class Strategy(Base):
    __tablename__ = 'strategy'
    __table_args__ = (
        Index('strategy_Date_strategyName_factor_uindex', 'Date', 'strategyName', 'factor', unique=True),
    )

    Date = Column(DateTime, primary_key=True, nullable=False)
    strategyName = Column(String(20, 'utf8_general_ci'), primary_key=True, nullable=False)
    factor = Column(String(50, 'utf8_general_ci'), primary_key=True, nullable=False)
    weight = Column(Float(53))
    source = Column(String(20, 'utf8_general_ci'))


class Tiny(Base):
    __tablename__ = 'tiny'

    Date = Column(DateTime, primary_key=True, nullable=False, server_default=text("(NULL)"))
    Code = Column(Integer, primary_key=True, nullable=False, server_default=text("(NULL)"))
    CFinc1 = Column(Float(53), server_default=text("(NULL)"))
    BDTO = Column(Float(53), server_default=text("(NULL)"))
    RVOL = Column(Float(53), server_default=text("(NULL)"))
    CHV = Column(Float(53), server_default=text("(NULL)"))
    VAL = Column(Float(53))
    EPSAfterNonRecurring = Column(Float(53))
    DivP = Column(Float(53))


class Universe(Base):
    __tablename__ = 'universe'
    __table_args__ = (
        Index('universe_Date_universe_Code_uindex', 'Date', 'universe', 'Code', unique=True),
    )

    Date = Column(DateTime, primary_key=True, nullable=False)
    Code = Column(Integer, primary_key=True, nullable=False)
    universe = Column(String(20, 'utf8_general_ci'), primary_key=True, nullable=False)


class Uqer(Base):
    __tablename__ = 'uqer'
    __table_args__ = (
        Index('factors_Date_Code_uindex', 'Date', 'Code', unique=True),
    )

    Date = Column(DateTime, primary_key=True, nullable=False)
    Code = Column(Integer, primary_key=True, nullable=False)
    AccountsPayablesTDays = Column(Float(53))
    AccountsPayablesTRate = Column(Float(53))
    AdminiExpenseRate = Column(Float(53))
    ARTDays = Column(Float(53))
    ARTRate = Column(Float(53))
    ASSI = Column(Float(53))
    BLEV = Column(Float(53))
    BondsPayableToAsset = Column(Float(53))
    CashRateOfSales = Column(Float(53))
    CashToCurrentLiability = Column(Float(53))
    CMRA = Column(Float(53))
    CTOP = Column(Float(53))
    CTP5 = Column(Float(53))
    CurrentAssetsRatio = Column(Float(53))
    CurrentAssetsTRate = Column(Float(53))
    CurrentRatio = Column(Float(53))
    DAVOL10 = Column(Float(53))
    DAVOL20 = Column(Float(53))
    DAVOL5 = Column(Float(53))
    DDNBT = Column(Float(53))
    DDNCR = Column(Float(53))
    DDNSR = Column(Float(53))
    DebtEquityRatio = Column(Float(53))
    DebtsAssetRatio = Column(Float(53))
    DHILO = Column(Float(53))
    DilutedEPS = Column(Float(53))
    DVRAT = Column(Float(53))
    EBITToTOR = Column(Float(53))
    EGRO = Column(Float(53))
    EMA10 = Column(Float(53))
    EMA120 = Column(Float(53))
    EMA20 = Column(Float(53))
    EMA5 = Column(Float(53))
    EMA60 = Column(Float(53))
    EPS = Column(Float(53))
    EquityFixedAssetRatio = Column(Float(53))
    EquityToAsset = Column(Float(53))
    EquityTRate = Column(Float(53))
    ETOP = Column(Float(53))
    ETP5 = Column(Float(53))
    FinancialExpenseRate = Column(Float(53))
    FinancingCashGrowRate = Column(Float(53))
    FixAssetRatio = Column(Float(53))
    FixedAssetsTRate = Column(Float(53))
    GrossIncomeRatio = Column(Float(53))
    HBETA = Column(Float(53))
    HSIGMA = Column(Float(53))
    IntangibleAssetRatio = Column(Float(53))
    InventoryTDays = Column(Float(53))
    InventoryTRate = Column(Float(53))
    InvestCashGrowRate = Column(Float(53))
    LCAP = Column(Float(53))
    LFLO = Column(Float(53))
    LongDebtToAsset = Column(Float(53))
    LongDebtToWorkingCapital = Column(Float(53))
    LongTermDebtToAsset = Column(Float(53))
    MA10 = Column(Float(53))
    MA120 = Column(Float(53))
    MA20 = Column(Float(53))
    MA5 = Column(Float(53))
    MA60 = Column(Float(53))
    MAWVAD = Column(Float(53))
    MFI = Column(Float(53))
    MLEV = Column(Float(53))
    NetAssetGrowRate = Column(Float(53))
    NetProfitGrowRate = Column(Float(53))
    NetProfitRatio = Column(Float(53))
    NOCFToOperatingNI = Column(Float(53))
    NonCurrentAssetsRatio = Column(Float(53))
    NPParentCompanyGrowRate = Column(Float(53))
    NPToTOR = Column(Float(53))
    OperatingExpenseRate = Column(Float(53))
    OperatingProfitGrowRate = Column(Float(53))
    OperatingProfitRatio = Column(Float(53))
    OperatingProfitToTOR = Column(Float(53))
    OperatingRevenueGrowRate = Column(Float(53))
    OperCashGrowRate = Column(Float(53))
    OperCashInToCurrentLiability = Column(Float(53))
    PB = Column(Float(53))
    PCF = Column(Float(53))
    PE = Column(Float(53))
    PS = Column(Float(53))
    PSY = Column(Float(53))
    QuickRatio = Column(Float(53))
    REVS10 = Column(Float(53))
    REVS20 = Column(Float(53))
    REVS5 = Column(Float(53))
    ROA = Column(Float(53))
    ROA5 = Column(Float(53))
    ROE = Column(Float(53))
    ROE5 = Column(Float(53))
    RSI = Column(Float(53))
    RSTR12 = Column(Float(53))
    RSTR24 = Column(Float(53))
    SalesCostRatio = Column(Float(53))
    SaleServiceCashToOR = Column(Float(53))
    SUE = Column(Float(53))
    TaxRatio = Column(Float(53))
    TOBT = Column(Float(53))
    TotalAssetGrowRate = Column(Float(53))
    TotalAssetsTRate = Column(Float(53))
    TotalProfitCostRatio = Column(Float(53))
    TotalProfitGrowRate = Column(Float(53))
    VOL10 = Column(Float(53))
    VOL120 = Column(Float(53))
    VOL20 = Column(Float(53))
    VOL240 = Column(Float(53))
    VOL5 = Column(Float(53))
    VOL60 = Column(Float(53))
    WVAD = Column(Float(53))
    REC = Column(Float(53))
    DAREC = Column(Float(53))
    GREC = Column(Float(53))
    FY12P = Column(Float(53))
    DAREV = Column(Float(53))
    GREV = Column(Float(53))
    SFY12P = Column(Float(53))
    DASREV = Column(Float(53))
    GSREV = Column(Float(53))
    FEARNG = Column(Float(53))
    FSALESG = Column(Float(53))
    TA2EV = Column(Float(53))
    CFO2EV = Column(Float(53))
    ACCA = Column(Float(53))
    DEGM = Column(Float(53))
    SUOI = Column(Float(53))
    EARNMOM = Column(Float(53))
    FiftyTwoWeekHigh = Column(Float(53))
    Volatility = Column(Float(53))
    Skewness = Column(Float(53))
    ILLIQUIDITY = Column(Float(53))
    BackwardADJ = Column(Float(53))
    MACD = Column(Float(53))
    ADTM = Column(Float(53))
    ATR14 = Column(Float(53))
    ATR6 = Column(Float(53))
    BIAS10 = Column(Float(53))
    BIAS20 = Column(Float(53))
    BIAS5 = Column(Float(53))
    BIAS60 = Column(Float(53))
    BollDown = Column(Float(53))
    BollUp = Column(Float(53))
    CCI10 = Column(Float(53))
    CCI20 = Column(Float(53))
    CCI5 = Column(Float(53))
    CCI88 = Column(Float(53))
    KDJ_K = Column(Float(53))
    KDJ_D = Column(Float(53))
    KDJ_J = Column(Float(53))
    ROC6 = Column(Float(53))
    ROC20 = Column(Float(53))
    SBM = Column(Float(53))
    STM = Column(Float(53))
    UpRVI = Column(Float(53))
    DownRVI = Column(Float(53))
    RVI = Column(Float(53))
    SRMI = Column(Float(53))
    ChandeSD = Column(Float(53))
    ChandeSU = Column(Float(53))
    CMO = Column(Float(53))
    DBCD = Column(Float(53))
    ARC = Column(Float(53))
    OBV = Column(Float(53))
    OBV6 = Column(Float(53))
    OBV20 = Column(Float(53))
    TVMA20 = Column(Float(53))
    TVMA6 = Column(Float(53))
    TVSTD20 = Column(Float(53))
    TVSTD6 = Column(Float(53))
    VDEA = Column(Float(53))
    VDIFF = Column(Float(53))
    VEMA10 = Column(Float(53))
    VEMA12 = Column(Float(53))
    VEMA26 = Column(Float(53))
    VEMA5 = Column(Float(53))
    VMACD = Column(Float(53))
    VOSC = Column(Float(53))
    VR = Column(Float(53))
    VROC12 = Column(Float(53))
    VROC6 = Column(Float(53))
    VSTD10 = Column(Float(53))
    VSTD20 = Column(Float(53))
    KlingerOscillator = Column(Float(53))
    MoneyFlow20 = Column(Float(53))
    AD = Column(Float(53))
    AD20 = Column(Float(53))
    AD6 = Column(Float(53))
    CoppockCurve = Column(Float(53))
    ASI = Column(Float(53))
    ChaikinOscillator = Column(Float(53))
    ChaikinVolatility = Column(Float(53))
    EMV14 = Column(Float(53))
    EMV6 = Column(Float(53))
    plusDI = Column(Float(53))
    minusDI = Column(Float(53))
    ADX = Column(Float(53))
    ADXR = Column(Float(53))
    Aroon = Column(Float(53))
    AroonDown = Column(Float(53))
    AroonUp = Column(Float(53))
    DEA = Column(Float(53))
    DIFF = Column(Float(53))
    DDI = Column(Float(53))
    DIZ = Column(Float(53))
    DIF = Column(Float(53))
    MTM = Column(Float(53))
    MTMMA = Column(Float(53))
    PVT = Column(Float(53))
    PVT6 = Column(Float(53))
    PVT12 = Column(Float(53))
    TRIX5 = Column(Float(53))
    TRIX10 = Column(Float(53))
    UOS = Column(Float(53))
    MA10RegressCoeff12 = Column(Float(53))
    MA10RegressCoeff6 = Column(Float(53))
    PLRC6 = Column(Float(53))
    PLRC12 = Column(Float(53))
    SwingIndex = Column(Float(53))
    Ulcer10 = Column(Float(53))
    Ulcer5 = Column(Float(53))
    Hurst = Column(Float(53))
    ACD6 = Column(Float(53))
    ACD20 = Column(Float(53))
    EMA12 = Column(Float(53))
    EMA26 = Column(Float(53))
    APBMA = Column(Float(53))
    BBI = Column(Float(53))
    BBIC = Column(Float(53))
    TEMA10 = Column(Float(53))
    TEMA5 = Column(Float(53))
    MA10Close = Column(Float(53))
    AR = Column(Float(53))
    BR = Column(Float(53))
    ARBR = Column(Float(53))
    CR20 = Column(Float(53))
    MassIndex = Column(Float(53))
    BearPower = Column(Float(53))
    BullPower = Column(Float(53))
    Elder = Column(Float(53))
    NVI = Column(Float(53))
    PVI = Column(Float(53))
    RC12 = Column(Float(53))
    RC24 = Column(Float(53))
    JDQS20 = Column(Float(53))
    Variance20 = Column(Float(53))
    Variance60 = Column(Float(53))
    Variance120 = Column(Float(53))
    Kurtosis20 = Column(Float(53))
    Kurtosis60 = Column(Float(53))
    Kurtosis120 = Column(Float(53))
    Alpha20 = Column(Float(53))
    Alpha60 = Column(Float(53))
    Alpha120 = Column(Float(53))
    Beta20 = Column(Float(53))
    Beta60 = Column(Float(53))
    Beta120 = Column(Float(53))
    SharpeRatio20 = Column(Float(53))
    SharpeRatio60 = Column(Float(53))
    SharpeRatio120 = Column(Float(53))
    TreynorRatio20 = Column(Float(53))
    TreynorRatio60 = Column(Float(53))
    TreynorRatio120 = Column(Float(53))
    InformationRatio20 = Column(Float(53))
    InformationRatio60 = Column(Float(53))
    InformationRatio120 = Column(Float(53))
    GainVariance20 = Column(Float(53))
    GainVariance60 = Column(Float(53))
    GainVariance120 = Column(Float(53))
    LossVariance20 = Column(Float(53))
    LossVariance60 = Column(Float(53))
    LossVariance120 = Column(Float(53))
    GainLossVarianceRatio20 = Column(Float(53))
    GainLossVarianceRatio60 = Column(Float(53))
    GainLossVarianceRatio120 = Column(Float(53))
    RealizedVolatility = Column(Float(53))
    REVS60 = Column(Float(53))
    REVS120 = Column(Float(53))
    REVS250 = Column(Float(53))
    REVS750 = Column(Float(53))
    REVS5m20 = Column(Float(53))
    REVS5m60 = Column(Float(53))
    REVS5Indu1 = Column(Float(53))
    REVS20Indu1 = Column(Float(53))
    Volumn1M = Column(Float(53))
    Volumn3M = Column(Float(53))
    Price1M = Column(Float(53))
    Price3M = Column(Float(53))
    Price1Y = Column(Float(53))
    Rank1M = Column(Float(53))
    CashDividendCover = Column(Float(53))
    DividendCover = Column(Float(53))
    DividendPaidRatio = Column(Float(53))
    RetainedEarningRatio = Column(Float(53))
    CashEquivalentPS = Column(Float(53))
    DividendPS = Column(Float(53))
    EPSTTM = Column(Float(53))
    NetAssetPS = Column(Float(53))
    TORPS = Column(Float(53))
    TORPSLatest = Column(Float(53))
    OperatingRevenuePS = Column(Float(53))
    OperatingRevenuePSLatest = Column(Float(53))
    OperatingProfitPS = Column(Float(53))
    OperatingProfitPSLatest = Column(Float(53))
    CapitalSurplusFundPS = Column(Float(53))
    SurplusReserveFundPS = Column(Float(53))
    UndividedProfitPS = Column(Float(53))
    RetainedEarningsPS = Column(Float(53))
    OperCashFlowPS = Column(Float(53))
    CashFlowPS = Column(Float(53))
    NetNonOIToTP = Column(Float(53))
    NetNonOIToTPLatest = Column(Float(53))
    PeriodCostsRate = Column(Float(53))
    InterestCover = Column(Float(53))
    NetProfitGrowRate3Y = Column(Float(53))
    NetProfitGrowRate5Y = Column(Float(53))
    OperatingRevenueGrowRate3Y = Column(Float(53))
    OperatingRevenueGrowRate5Y = Column(Float(53))
    NetCashFlowGrowRate = Column(Float(53))
    NetProfitCashCover = Column(Float(53))
    OperCashInToAsset = Column(Float(53))
    CashConversionCycle = Column(Float(53))
    OperatingCycle = Column(Float(53))
    PEG3Y = Column(Float(53))
    PEG5Y = Column(Float(53))
    PEIndu = Column(Float(53))
    PBIndu = Column(Float(53))
    PSIndu = Column(Float(53))
    PCFIndu = Column(Float(53))
    PEHist20 = Column(Float(53))
    PEHist60 = Column(Float(53))
    PEHist120 = Column(Float(53))
    PEHist250 = Column(Float(53))
    StaticPE = Column(Float(53))
    ForwardPE = Column(Float(53))
    EnterpriseFCFPS = Column(Float(53))
    ShareholderFCFPS = Column(Float(53))
    ROEDiluted = Column(Float(53))
    ROEAvg = Column(Float(53))
    ROEWeighted = Column(Float(53))
    ROECut = Column(Float(53))
    ROECutWeighted = Column(Float(53))
    ROIC = Column(Float(53))
    ROAEBIT = Column(Float(53))
    ROAEBITTTM = Column(Float(53))
    OperatingNIToTP = Column(Float(53))
    OperatingNIToTPLatest = Column(Float(53))
    InvestRAssociatesToTP = Column(Float(53))
    InvestRAssociatesToTPLatest = Column(Float(53))
    NPCutToNP = Column(Float(53))
    SuperQuickRatio = Column(Float(53))
    TSEPToInterestBearDebt = Column(Float(53))
    DebtTangibleEquityRatio = Column(Float(53))
    TangibleAToInteBearDebt = Column(Float(53))
    TangibleAToNetDebt = Column(Float(53))
    NOCFToTLiability = Column(Float(53))
    NOCFToInterestBearDebt = Column(Float(53))
    NOCFToNetDebt = Column(Float(53))
    TSEPToTotalCapital = Column(Float(53))
    InteBearDebtToTotalCapital = Column(Float(53))
    NPParentCompanyCutYOY = Column(Float(53))
    SalesServiceCashToORLatest = Column(Float(53))
    CashRateOfSalesLatest = Column(Float(53))
    NOCFToOperatingNILatest = Column(Float(53))
    TotalAssets = Column(Float(53))
    MktValue = Column(Float(53))
    NegMktValue = Column(Float(53))
    TEAP = Column(Float(53))
    NIAP = Column(Float(53))
    TotalFixedAssets = Column(Float(53))
    IntFreeCL = Column(Float(53))
    IntFreeNCL = Column(Float(53))
    IntCL = Column(Float(53))
    IntDebt = Column(Float(53))
    NetDebt = Column(Float(53))
    NetTangibleAssets = Column(Float(53))
    WorkingCapital = Column(Float(53))
    NetWorkingCapital = Column(Float(53))
    TotalPaidinCapital = Column(Float(53))
    RetainedEarnings = Column(Float(53))
    OperateNetIncome = Column(Float(53))
    ValueChgProfit = Column(Float(53))
    NetIntExpense = Column(Float(53))
    EBIT = Column(Float(53))
    EBITDA = Column(Float(53))
    EBIAT = Column(Float(53))
    NRProfitLoss = Column(Float(53))
    NIAPCut = Column(Float(53))
    FCFF = Column(Float(53))
    FCFE = Column(Float(53))
    DA = Column(Float(53))
    TRevenueTTM = Column(Float(53))
    TCostTTM = Column(Float(53))
    RevenueTTM = Column(Float(53))
    CostTTM = Column(Float(53))
    GrossProfitTTM = Column(Float(53))
    SalesExpenseTTM = Column(Float(53))
    AdminExpenseTTM = Column(Float(53))
    FinanExpenseTTM = Column(Float(53))
    AssetImpairLossTTM = Column(Float(53))
    NPFromOperatingTTM = Column(Float(53))
    NPFromValueChgTTM = Column(Float(53))
    OperateProfitTTM = Column(Float(53))
    NonOperatingNPTTM = Column(Float(53))
    TProfitTTM = Column(Float(53))
    NetProfitTTM = Column(Float(53))
    NetProfitAPTTM = Column(Float(53))
    SaleServiceRenderCashTTM = Column(Float(53))
    NetOperateCFTTM = Column(Float(53))
    NetInvestCFTTM = Column(Float(53))
    NetFinanceCFTTM = Column(Float(53))
    GrossProfit = Column(Float(53))
    Beta252 = Column(Float(53))
    RSTR504 = Column(Float(53))
    EPIBS = Column(Float(53))
    CETOP = Column(Float(53))
    DASTD = Column(Float(53))
    CmraCNE5 = Column(Float(53))
    HsigmaCNE5 = Column(Float(53))
    SGRO = Column(Float(53))
    EgibsLong = Column(Float(53))
    STOM = Column(Float(53))
    STOQ = Column(Float(53))
    STOA = Column(Float(53))
    NLSIZE = Column(Float(53))


if __name__ == '__main__':

    from sqlalchemy import create_engine

    engine = create_engine('mysql+mysqldb://sa:We051253524522@rm-bp1psdz5615icqc0yo.mysql.rds.aliyuncs.com/test?charset=utf8')
    Base.metadata.create_all(engine)
